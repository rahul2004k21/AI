class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment
        self.position = 0

    def move_left(self):
        if self.position > 0:
            self.position -= 1

    def move_right(self):
        if self.position < len(self.environment) - 1:
            self.position += 1

    def clean(self):
        self.environment[self.position] = 'clean'

    def perceive(self):
        return self.environment[self.position]

def clean_environment(environment):
    cleaner = VacuumCleaner(environment)
    cleaned = 0
    total = len(environment)

    while cleaned < total:
        state = cleaner.perceive()
        if state == 'dirty':
            cleaner.clean()
            cleaned += 1
        elif state == 'clean':
            pass

        if cleaner.position == 0:
            cleaner.move_right()
        else:
            cleaner.move_left()

    print("Environment cleaned successfully.")

if __name__ == "__main__":
    # Example environment: 'dirty' represents a dirty square, 'clean' represents a clean square
    environment = ['dirty', 'clean', 'dirty', 'clean', 'dirty', 'clean']
    clean_environment(environment)
