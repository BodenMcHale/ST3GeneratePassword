from random import sample, choice, randrange

class PasswordCommand(sublime_plugin.TextCommand):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*_-+=|/?:;<>~"
    length = randrange(6, 31)

    def run(self, edit):
        population = self.chars
        for region in self.view.sel():
            p = ''.join(sample(population, self.length))
            self.view.replace(edit, region, p)

class GenerateTinyPasswordCommand(PasswordCommand):
    length = 5

class GenerateShortPasswordCommand(PasswordCommand):
    length = 10

class GenerateMediumPasswordCommand(PasswordCommand):
    length = 15

class GenerateLongPasswordCommand(PasswordCommand):
    length = 20