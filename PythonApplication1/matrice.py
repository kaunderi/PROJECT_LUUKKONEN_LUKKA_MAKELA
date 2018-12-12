import easygopigo3 as easy


class RobotMovement(object):
    """docstring for RobotMovement"""
    def __init__(self):
        super(RobotMovement, self).__init__()
        self.gpg = easy.EasyGoPiGo3()
        self.my_distance_sensor = self.gpg.init_distance_sensor()
        self.matrix = [[0, 0, 0, 0, ],
                       [0, 0, 0, 0, ],
                       [0, 0, 0, 0, ],
                       [0, 0, 0, 0, ]]
        self.current_position = [0][0]
        self.x = 0
        self.y = 0
        self.start = [0][0]
        self.goal = [0][0]
        self.degree = 90
        self.distance = 30

    def print_matrix(self):
        for row in self.matrix:
            print(' '.join(map(str, row)))

    def object_detected(self):
        input("Kääntyy")
        self.gpg.turn_degrees(self.degree)
        if self.object_detection(self.distance):
            self.gpg.turn_degrees(self.degree)
            if not self.object_detection(self.distance):
                self.gpg.drive_cm(self.distance)
                self.y += 1
        else:
            self.gpg.drive_cm(self.distance)
            self.y += 1
            self.gpg.turn_degrees(-self.degree)

    def forward(self, distance):
        if self.object_detection(distance):
            self.matrix[self.x + 1][self.y] = 1
            print(self.matrix[self.x + 1][self.y])
            print("Object detected")
            self.object_detected()
        else:
            print("Going forward")
            self.gpg.drive_cm(distance)
            self.x += 1
            self.matrix[self.x][self.y] = 0

    def object_detection(self, distance):
        measurement = self.my_distance_sensor.read_mm()
        if measurement < distance * 10:
            return True
        else:
            return False

    def matrix_mapping(self):
        self.current_position = self.matrix[self.x][self.y]
        print(self.current_position)

    def run(self):
        self.forward(30)
        self.print_matrix()


def main():
    gpg = RobotMovement()
    while True:
        gpg.run()
        gpg.matrix_mapping()
        input()


if __name__ == '__main__':
    main()