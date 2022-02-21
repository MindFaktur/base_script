from basescript import BaseScript


class Adder(BaseScript):

    DESC = "adds numbers"

    def __init__(self):
        super().__init__()
        self.a = 10
        self.b = 20

    def define_args(self, parser):
        parser.add_argument('c', type=int, help='number to add')

    def run(self):
        self.log.info('running script')
        print(self.a + self.b + self.args.c)
        self.log.info('script finished')


if __name__ == '__main__':
    Adder().start()
