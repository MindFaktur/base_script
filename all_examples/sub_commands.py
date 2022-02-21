from basescript import BaseScript


class SubCommands(BaseScript):

    A = 10

    def add(self):
        """
        Add the given value to the initial value
        :return: nothing
        """
        print(self.A + self.args.b)

    def sub(self):
        """
        Subtract the given value
        :return: nothing
        """
        print(f"subtarct value of {self.A} - {self.args.b} is {self.A - self.args.b}")

    def define_subcommands(self, subcommands):
        """
        defines sub commands
        :param subcommands:
        :return: nothing
        """
        super().define_subcommands(subcommands)

        add_command = subcommands.add_parser('add', help="Add's numbers")
        add_command.set_defaults(func=self.add)
        add_command.add_argument('--b', type=int, help='number to add')

        subtract_cmd = subcommands.add_parser('sub', help='Subtract number')
        subtract_cmd.set_defaults(func=self.sub)
        subtract_cmd.add_argument('--b', type=int, help='Number to subtract')


if __name__ == '__main__':
    SubCommands().start()
