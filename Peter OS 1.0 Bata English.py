print('Weicome To Use Peter OS 1.0 Bata Linux System')
Boot = float(input('Whether or not to use Peter OS 1.0 Bata Linux System，Please Press The Boot 1 ，Shut Down Please Press Any Key（1 except）。Please Write：'))
if (Boot == 1):
    print('The Computer Has Been Booted,Please Select The Software To Use。', '1.Phone', '2.E-mall', '3.Transfer', '4.Coming Soon')
    Software = int(input('Please Enter：'))
    if (Software == 1):
        print('The Phone Is Open,Please Enter The Number You Want To Dial')
        Boot = str(input('Please Enter：'))
        print('Is Dialing', input())
        Hung = int(input('To Hang Up,Press 1.Please Enter：'))
        if (Hung == 1):
            print('Has Been Hung Up')
    if (Software == 2):
        print('The E-mall Has Been Opened.Please Enter The Receiver:')
        Emall = str(input('Please Enter：'))
        Send = str(input('Please Enter What You Want To Send：'))
        print('Has Been Sent To The', Emall, Send)
    if (Software == 3):
        print('The Transfer Has Been Opened.Please Enter The Beneflciary Account：')
        Beneflciary = str(input('Please Enter The Beneflciary Account：'))
        Amount = str(input('Please Enter The Amount：'))
        print('Transferred', Beneflciary, Amount)
else:
    print('Computer Was Shut Down')
