from robot import robot
import json, boto3, os


class parser():

    def __init__(self):
        s3 = boto3.resource('s3')
        s3.meta.client.download_file(os.environ['s3Bucket'], 'instruction.txt', '/tmp/instruction.txt')
        f = open("/tmp/instruction.txt", "r")
        self.commands = f.readlines()
        self.place = "PLACE"

    def refine_commands(self):
        """
         This method is used to refine commands and look for first place command
        :return: list of commands
        """
        while (True):

            if (self.place in self.commands[0]):
                return self.commands
            else:
                self.commands.pop(0)

        return self.commands

    def get_placement(self):
        self.refine_commands()
        placeMent = self.commands[0].split(" ")
        p = placeMent[1].split(",")
        self.commands.pop(0)

        return p[0], p[1], p[2].strip("\n")


def lambda_handler(event, context):
    p = parser()
    x, y, d = (p.get_placement())
    r = robot(int(x), int(y), d)

    if (r.check_initial_placement()):
        for command in p.commands:

            if (command == "REPORT"):
                print(r.x, r.y, r.direction)
                return {
                    "statusCode": 200,
                    "body": json.dumps({
                        "x": r.x,
                        "y": r.y,
                        "direction": r.direction
                    }),
                }
            else:
                r.decision_maker(command.strip("\n"))
    else:
        print ("Robot is not placed correctly")
        return {
            "statusCode": 200,
            "body": json.dumps({
                "x": r.x,
                "y": r.y,
                "direction": r.direction,
                "observation": "initial placement is not on control plane"
            }),
        }
