#percabangan dengan dictionary
#swift case
#cara ini tidak pythonic
# def satu() :
#     print('satusatu')
# def dua():
#     print('duadua')
# def tiga():
#     print('tigatiga')
#
# case = 'satu'
# if case == 'satu' :
#     satu()
# elif case == 'dua' :
#     dua()
# elif case  == 'tiga':
#     tiga()

def satu() :
    print('satu nih bos')
def dua():
    print('dua nih bos')
def tiga():
    print('tiga nih bos')
case = 'dua'
#tidak perlu di beri tanda kurung
switch = {
    'satu':satu,  #'key:value,
    'dua':dua,
    'tiga':tiga,
}
switch[case]()