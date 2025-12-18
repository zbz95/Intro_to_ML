import glob

some_number = 100
some_list = [1,2,3]

def kvadrat(x):
    return x**2

class Oblast:
  def __init__(self, obl_name):
    self.files = glob.glob(f'/content/demo/*{obl_name}*')

  def count_ip(self, year):
    malyi, srednii, krupnyi = 0, 0, 0
    for file in self.files:
      if str(year) in file:
        with open(file) as f:
          f = f.readlines()

        for line in f:
          dohod = float(line[13:-1])
          if dohod < 200:
            malyi += 1
          elif dohod > 700:
            krupnyi += 1
          else:
            srednii += 1

    return {'malyi':malyi, 'srednii':srednii, 'krupnyi':krupnyi}
