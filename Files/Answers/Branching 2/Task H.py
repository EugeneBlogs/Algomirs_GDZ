n = int(input())
ticket_60 = n // 60
ticket_10 = (n % 60) // 10
ticket_1 = n % 10
if ticket_1 * 15 > 125:
    ticket_1 = 0
    ticket_10 += 1
if ticket_1 * 15 + ticket_10 * 125 > 440:
    ticket_1 = 0
    ticket_10 = 0
    ticket_60 += 1
print(ticket_1, ticket_10, ticket_60)
