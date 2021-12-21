# 62280101

from typing import Union

Number = Union[int, float]


def in_put(string: str = None):
    if string:
        return string
    return input()


def run(a: str, b: str):
    current_a = len(a)-1
    if not a:
        return True
    for b_letter in reversed(b):
        if current_a == 0:
            return True
        if b_letter == a[current_a]:
            current_a -= 1
    return False


def main(a: str = None, b: str = None):
    if not a or not b:
        a = 'qtqkcxytpoptpinnnzsywdkcxcevafs'
        b = 'hzwgejxespojukkupeiwxlnuojaoqrqrfgkccwtxukshxnldgxoeldgewtbqjdqmmelmlmtkfzhvxysbjkdqfhqwtmylrqtjocwnyxilzlzfzxshgdliuwszkksgqrzalmmznnwpijvgwyegtinhrueviqufjizbpzxpfqqvjytvxbvaqunumkclcdzhnawkxilubfzisberzvspunknmvvgkjilmgffefklsjgjugrccfpmxwemnzvsynhfjgskfgcdqmkawuhjbvvicevhlqrqlwghumqgvbdvujqmzygbvycqmoaqmodwjrwcootijhxehabnacmzcyjpyldqgrkplshelszsqluyafqqwvbkfbchpfvyregezibwsrfulueikahthpbnurkgedshtnedeqmpmcikxxwvttebkwblqvagtgsgxiegcmhimeeyeapecjszpwdruwtrxqobfnkieeaxsyxjxbvvjbgutrmhbdhoofquqxutmswffpuuuyurkrgmovdbdavkwfoedvqaimkgkvvqkzjvzmznmbcpxfoxteezivyhnxryculurbflolhvbiwsmgfzhkunrpbzqfqvdojjksbepfighundadzvhcdhuwegqbqyhcociehxlqgecnxpcufzveosrmfnlevgjlxazwmbwyaxcffxhihdekzyxnplxoazfdvsjtbopkwebmuocdagmgtqttgximtjlaigootdddpeqefwuizrcuzzzzzmmwinbdwtukpydrrgvzogexutcyofkdyclsktdiqdcvxpmfqbslshwkpoiyjtiokmgytnbbbvfqoqtiutzexccmdhxuzmfdtfmmtboizpfzatllnpjctwlkjqybhafavopqgtbiyxvzlvfhirdultyiamrobylmiisddmnqvqcbxtknznavv'

    result = run(a, b)
    return result


if __name__ == '__main__':
    a = in_put()
    b = in_put()
    print(main(a, b))
