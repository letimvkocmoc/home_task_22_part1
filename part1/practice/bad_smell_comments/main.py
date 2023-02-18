# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:

    def move(self, field, x_coord: int, y_coord: int, direction, is_fly: bool, is_creep: bool, speed_units: int = 1):

        if is_fly and is_creep:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed_units *= 1.2
            if direction == 'UP':
                new_y = y_coord + speed_units
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed_units
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord
            elif direction == 'RIGHT':
                new_y = y_coord
                new_x = x_coord + speed_units

        if is_creep:
            speed_units *= 0.5
            if direction == 'UP':
                new_y = y_coord + speed_units
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed_units
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed_units
            elif direction == 'RIGHT':
                new_y = y_coord
                new_x = x_coord + speed_units

            field.set_unit(x=new_x, y=new_y, unit=self)
