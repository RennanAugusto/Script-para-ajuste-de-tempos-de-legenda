import datetime as dt
from io import StringIO

class Adjust_Subtitles():

    def __init__(self, archive_name, adjustment_percentage):
        self.Archive_Name = archive_name
        self.Adjustment_Factor = adjustment_percentage / 100
        self.Format = '%H:%M:%S,%f'
        self.Buffer_Aux = StringIO()

    def adjust_subtitles(self):
        self.__apply_factor()
        self.__save_modifications()

    def __get_hora_legenda(self, hour):
        hour = hour.replace('\n', '')
        hour_aux = dt.datetime.strptime(hour, self.Format)
        hour_aux = dt.timedelta(seconds=hour_aux.second, hours=hour_aux.hour, minutes=hour_aux.minute,
                                microseconds=hour_aux.microsecond)
        return hour_aux


    def __get_str_timedelfa(self, timedelta):
        hour_str = timedelta.__str__()

        if len(hour_str) > 12:
            hour_str = hour_str[:-3]

        hour_str = hour_str.replace('.', ',')
        return  hour_str

    def __apply_factor(self):
        with open(self.Archive_Name, 'r') as file:
            for line in file:
                if line.__contains__('-->'):
                    line_aux = line.split(' --> ')
                    new_line = ''
                    for hour in line_aux:
                        hour_aux = self.__get_hora_legenda(hour)
                        hour_aux = hour_aux + (hour_aux * self.Adjustment_Factor)
                        hour_str = self.__get_str_timedelfa(hour_aux)
                        new_line += (hour_str + ' --> ' if new_line == '' else hour_str + '\n')
                    self.Buffer_Aux.write(new_line)
                else:
                    self.Buffer_Aux.write(line)

    def __save_modifications(self):
        with open(self.Archive_Name, 'w') as file:
            file.write(self.Buffer_Aux.getvalue())

ajuste = Adjust_Subtitles('Venom.srt', 1)
ajuste.adjust_subtitles()
# nome_arquivo = 'Venom.srt'
# arquivo = open(nome_arquivo, 'r')
# format = '%H:%M:%S,%f'
# percentual = 1 / 100
#
# buffer = StringIO()
#
# for line in arquivo:
#     if line.__contains__('-->'):
#         line_aux = line.split('-->')
#         new_line = ''
#         for hour in line_aux:
#             hour = hour.replace(' ', '')
#             hour = hour.replace('\n', '')
#             hour_aux = dt.datetime.strptime(hour, '%H:%M:%S,%f')
#             teste = dt.timedelta(seconds=hour_aux.second, hours=hour_aux.hour, minutes=hour_aux.minute, microseconds=hour_aux.microsecond)
#             # hour_aux = hour_aux.timed
#             # hour_aux = hour_aux * percentual
#             hour_aux = teste + (teste * percentual)
#             hour_str = hour_aux.__str__()
#             hour_str = hour_str[:-3]
#             new_line += (hour_str + ' --> ' if new_line == '' else hour_str + '\n')
#         buffer.write(new_line)
#     else:
#         buffer.write(line)
#
# arquivo.close()
#
# arquivo = open(nome_arquivo, 'w')
# str = buffer.getvalue()
# arquivo.write(buffer.getvalue())
#
# arquivo.close()

