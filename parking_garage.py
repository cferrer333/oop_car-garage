class ParkingGarage:

    def __init__(self, tickets=200, parkingSpaces=200, currentTicket={'paid':False}):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self):
        print('Please, take your ticket.')
        self.tickets -= 1
        self.parkingSpaces -= 1

    def payForParking(self):
        payment = input('Please, make a payment of $5: ')
        if payment.lower() != '':
            self.currentTicket['paid'] = True
            print('You have 15 minutes to leave the garage.')
            self.leaveGarage()
        else:
            self.leaveGarage()

    def leaveGarage(self):
        if self.currentTicket['paid']:
            print('Thank you, have a nice day!')
            self.currentTicket['paid'] = False
            self.tickets += 1
            self.parkingSpaces += 1
        else:
            print('Please, pay your ticket')
            self.payForParking()


garage = ParkingGarage()


def run():
    while True:
        response = input('What would you like to do? (Take ticket, Pay for parking, Cancel) ')
        if response.lower() == 'take ticket':
            garage.takeTicket()
        elif response.lower() == 'pay for parking':
            garage.payForParking()
        elif response.lower() == 'cancel':
            break
        else:
            print("Not a valid response.")


run()


