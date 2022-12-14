from app.models import db, Transaction
from datetime import date


def seed_transactions(
):  # this is the function that will seed the transactions for the database and the transactions table
    philz_one = Transaction(trans_date=date(2022, 1, 17),
                            trans_payee='Philz Coffee',
                            trans_amount=6.02,
                            categoryId=6,
                            accountId=2)
    philz_two = Transaction(trans_date=date(2022, 1, 7),
                            trans_payee='Philz Coffee',
                            trans_amount=6.02,
                            categoryId=6,
                            accountId=2)
    philz_three = Transaction(trans_date=date(2022, 1, 9),
                              trans_payee='Philz Coffee',
                              trans_amount=5.27,
                              categoryId=6,
                              accountId=3)
    philz_four = Transaction(trans_date=date(2022, 2, 6),
                             trans_payee='Philz Coffee',
                             trans_amount=6.13,
                             categoryId=6,
                             accountId=3)
    starbucks = Transaction(trans_date=date(2022, 2, 1),
                            trans_payee='Starbucks',
                            trans_amount=12.78,
                            categoryId=6,
                            accountId=2)
    starbucks_two = Transaction(trans_date=date(2022, 2, 11),
                                trans_payee='Starbucks',
                                trans_amount=10.56,
                                categoryId=6,
                                accountId=3)
    bevmo = Transaction(trans_date=date(2022, 2, 13),
                        trans_payee='BevMo!',
                        trans_amount=18.34,
                        categoryId=6,
                        accountId=3)
    starbucks_three = Transaction(trans_date=date(2022, 2, 16),
                                  trans_payee='Starbucks',
                                  trans_amount=11.28,
                                  categoryId=6,
                                  accountId=2)
    philz_five = Transaction(trans_date=date(2022, 2, 20),
                             trans_payee='Philz Coffee',
                             trans_amount=7.40,
                             categoryId=6,
                             accountId=4)
    boba = Transaction(trans_date=date(2022, 2, 22),
                       trans_payee='Boba Guys',
                       trans_amount=6.36,
                       categoryId=6,
                       accountId=2)
    starbucks_four = Transaction(trans_date=date(2022, 2, 25),
                                 trans_payee='Starbucks',
                                 trans_amount=8.77,
                                 categoryId=6,
                                 accountId=2)
    philz_six = Transaction(trans_date=date(2022, 3, 4),
                            trans_payee='Philz Coffee',
                            trans_amount=26.34,
                            categoryId=6,
                            accountId=3)
    starbucks_five = Transaction(trans_date=date(2022, 3, 14),
                                 trans_payee='Starbucks',
                                 trans_amount=12.08,
                                 categoryId=6,
                                 accountId=4)
    tonga = Transaction(trans_date=date(2022, 3, 12),
                        trans_payee='Tonga Room',
                        trans_amount=23.51,
                        categoryId=6,
                        accountId=2)
    philz_seven = Transaction(trans_date=date(2022, 4, 2),
                              trans_payee='Philz Coffee',
                              trans_amount=11.17,
                              categoryId=6,
                              accountId=3)
    starbucks_six = Transaction(trans_date=date(2022, 4, 7),
                                trans_payee='Starbucks',
                                trans_amount=12.47,
                                categoryId=6,
                                accountId=2)

    chipotle_one = Transaction(trans_date=date(2022, 1, 13),
                               trans_payee='Chipotle',
                               trans_amount=8.59,
                               categoryId=6,
                               accountId=2)
    chipotle_two = Transaction(trans_date=date(2022, 1, 18),
                               trans_payee='Chipotle',
                               trans_amount=10.46,
                               categoryId=6,
                               accountId=4)
    chipotle_three = Transaction(trans_date=date(2022, 2, 8),
                                 trans_payee='Chipotle',
                                 trans_amount=16.92,
                                 categoryId=6,
                                 accountId=4)
    shake_shack = Transaction(trans_date=date(2022, 2, 4),
                              trans_payee='Shake Shack',
                              trans_amount=13.88,
                              categoryId=6,
                              accountId=4)
    bojangles = Transaction(trans_date=date(2022, 2, 10),
                            trans_payee='Bojangles',
                            trans_amount=12.72,
                            categoryId=6,
                            accountId=4)
    buffalo = Transaction(trans_date=date(2022, 2, 13),
                          trans_payee='Wingstop',
                          trans_amount=26.69,
                          categoryId=6,
                          accountId=4)
    chipotle_four = Transaction(trans_date=date(2022, 2, 15),
                                trans_payee='Chipotle',
                                trans_amount=12.67,
                                categoryId=6,
                                accountId=3)
    chipotle_five = Transaction(trans_date=date(2022, 2, 23),
                                trans_payee='Chipotle',
                                trans_amount=11.14,
                                categoryId=6,
                                accountId=4)
    portillos = Transaction(trans_date=date(2022, 2, 26),
                            trans_payee='Portillos',
                            trans_amount=18.55,
                            categoryId=6,
                            accountId=4)
    inNOut = Transaction(trans_date=date(2022, 3, 2),
                         trans_payee='In-N-Out',
                         trans_amount=9.36,
                         categoryId=6,
                         accountId=3)
    chipotle_six = Transaction(trans_date=date(2022, 3, 6),
                               trans_payee='Chipotle',
                               trans_amount=11.72,
                               categoryId=6,
                               accountId=2)
    shake_shack_two = Transaction(trans_date=date(2022, 3, 8),
                                  trans_payee='Shake Shack',
                                  trans_amount=12.01,
                                  categoryId=6,
                                  accountId=3)
    portillos_two = Transaction(trans_date=date(2022, 3, 13),
                                trans_payee='Portillos',
                                trans_amount=15.26,
                                categoryId=6,
                                accountId=2)
    chipotle_seven = Transaction(trans_date=date(2022, 4, 5),
                                 trans_payee='Chipotle',
                                 trans_amount=12.64,
                                 categoryId=6,
                                 accountId=2)
    portillos_three = Transaction(trans_date=date(2022, 4, 9),
                                  trans_payee='Portillos',
                                  trans_amount=15.53,
                                  categoryId=6,
                                  accountId=4)

    trader_joes = Transaction(trans_date=date(2022, 1, 13),
                              trans_payee='Trader Joes',
                              trans_amount=20.56,
                              categoryId=13,
                              accountId=2)
    whole_foods = Transaction(trans_date=date(2022, 1, 1),
                              trans_payee='Whole Foods',
                              trans_amount=23.40,
                              categoryId=13,
                              accountId=3)
    whole_foods_two = Transaction(trans_date=date(2022, 2, 2),
                                  trans_payee='Whole Foods',
                                  trans_amount=32.13,
                                  categoryId=13,
                                  accountId=3)
    costco = Transaction(trans_date=date(2022, 2, 3),
                         trans_payee='Costco',
                         trans_amount=41.58,
                         categoryId=13,
                         accountId=3)
    trader_joes_two = Transaction(trans_date=date(2022, 2, 19),
                                  trans_payee='Trader Joes',
                                  trans_amount=20.49,
                                  categoryId=13,
                                  accountId=4)
    costco_two = Transaction(trans_date=date(2022, 3, 2),
                             trans_payee='Costco',
                             trans_amount=68.89,
                             categoryId=13,
                             accountId=2)
    whole_foods_three = Transaction(trans_date=date(2022, 3, 5),
                                    trans_payee='Whole Foods',
                                    trans_amount=40.37,
                                    categoryId=13,
                                    accountId=4)
    costco_three = Transaction(trans_date=date(2022, 4, 6),
                               trans_payee='Costco',
                               trans_amount=97.14,
                               categoryId=13,
                               accountId=4)
    trader_joes_three = Transaction(trans_date=date(2022, 4, 8),
                                    trans_payee='Trader Joes',
                                    trans_amount=37.03,
                                    categoryId=13,
                                    accountId=4)

    chewy_one = Transaction(trans_date=date(2022, 1, 6),
                            trans_payee='Chewy.com',
                            trans_amount=30.98,
                            categoryId=18,
                            accountId=2)
    chewy_two = Transaction(trans_date=date(2022, 1, 12),
                            trans_payee='Chewy.com',
                            trans_amount=10.23,
                            categoryId=18,
                            accountId=2)
    chewy_three = Transaction(trans_date=date(2022, 2, 12),
                              trans_payee='Chewy.com',
                              trans_amount=22.97,
                              categoryId=18,
                              accountId=2)
    chewy_four = Transaction(trans_date=date(2022, 2, 21),
                             trans_payee='Chewy.com',
                             trans_amount=32.72,
                             categoryId=18,
                             accountId=3)
    chewy_five = Transaction(trans_date=date(2022, 3, 3),
                             trans_payee='Chewy.com',
                             trans_amount=29.97,
                             categoryId=18,
                             accountId=3)

    amazon_one = Transaction(trans_date=date(2022, 1, 8),
                             trans_payee='Amazon.com',
                             trans_amount=50.51,
                             categoryId=19,
                             accountId=2)
    amazon_two = Transaction(trans_date=date(2022, 1, 11),
                             trans_payee='Amazon.com',
                             trans_amount=12.80,
                             categoryId=19,
                             accountId=2)
    taylor_stitch = Transaction(trans_date=date(2022, 1, 8),
                                trans_payee='Taylor Stitch',
                                trans_amount=35.06,
                                categoryId=19,
                                accountId=5)
    drop = Transaction(trans_date=date(2022, 1, 19),
                       trans_payee='Drop',
                       trans_amount=23.57,
                       categoryId=19,
                       accountId=2)
    grailed = Transaction(trans_date=date(2022, 1, 14),
                          trans_payee='Grailed',
                          trans_amount=28.01,
                          categoryId=19,
                          accountId=3)
    everlane = Transaction(trans_date=date(2021, 12, 8),
                           trans_payee='Everlane',
                           trans_amount=51.76,
                           categoryId=19,
                           accountId=2)
    uniqlo = Transaction(trans_date=date(2021, 12, 14),
                         trans_payee='Uniqlo',
                         trans_amount=27.10,
                         categoryId=19,
                         accountId=2)
    amazon_three = Transaction(trans_date=date(2022, 2, 3),
                               trans_payee='Amazon.com',
                               trans_amount=17.34,
                               categoryId=19,
                               accountId=2)
    uniqlo_two = Transaction(trans_date=date(2022, 2, 7),
                             trans_payee='Uniqlo',
                             trans_amount=31.43,
                             categoryId=19,
                             accountId=2)
    danner = Transaction(trans_date=date(2022, 2, 14),
                         trans_payee='Danner',
                         trans_amount=121.53,
                         categoryId=19,
                         accountId=2)
    keychron = Transaction(trans_date=date(2022, 2, 15),
                           trans_payee='Keychron',
                           trans_amount=77.36,
                           categoryId=19,
                           accountId=3)
    pistol = Transaction(trans_date=date(2022, 2, 28),
                         trans_payee='Pistol Lake',
                         trans_amount=92.19,
                         categoryId=19,
                         accountId=5)
    amazon_four = Transaction(trans_date=date(2022, 2, 23),
                              trans_payee='Amazon.com',
                              trans_amount=33.41,
                              categoryId=19,
                              accountId=2)
    amazon_five = Transaction(trans_date=date(2022, 3, 1),
                              trans_payee='Amazon.com',
                              trans_amount=64.63,
                              categoryId=19,
                              accountId=3)
    rogue_territory = Transaction(trans_date=date(2022, 3, 6),
                                  trans_payee='Rogue Territory',
                                  trans_amount=426.67,
                                  categoryId=19,
                                  accountId=3)
    taylor_stitch_two = Transaction(trans_date=date(2022, 3, 11),
                                    trans_payee='Taylor Stitch',
                                    trans_amount=75.18,
                                    categoryId=19,
                                    accountId=5)
    amazon_six = Transaction(trans_date=date(2022, 4, 3),
                             trans_payee='Amazon.com',
                             trans_amount=112.01,
                             categoryId=19,
                             accountId=2)

    uber = Transaction(trans_date=date(2022, 1, 10),
                       trans_payee='Uber',
                       trans_amount=15.80,
                       categoryId=21,
                       accountId=3)
    lyft = Transaction(trans_date=date(2022, 1, 2),
                       trans_payee='Lyft',
                       trans_amount=12.61,
                       categoryId=21,
                       accountId=3)
    uber_two = Transaction(trans_date=date(2022, 2, 4),
                           trans_payee='Uber',
                           trans_amount=10.17,
                           categoryId=21,
                           accountId=3)
    lyft_two = Transaction(trans_date=date(2022, 2, 8),
                           trans_payee='Lyft',
                           trans_amount=14.89,
                           categoryId=21,
                           accountId=3)
    uber_three = Transaction(trans_date=date(2022, 2, 20),
                             trans_payee='Uber',
                             trans_amount=18.01,
                             categoryId=21,
                             accountId=2)
    lyft_three = Transaction(trans_date=date(2022, 3, 13),
                             trans_payee='Lyft',
                             trans_amount=16.05,
                             categoryId=21,
                             accountId=4)

    udemy_one = Transaction(trans_date=date(2022, 1, 9),
                            trans_payee='Udemy',
                            trans_amount=32.57,
                            categoryId=7,
                            accountId=3)
    udemy_two = Transaction(trans_date=date(2021, 12, 22),
                            trans_payee='Udemy',
                            trans_amount=28.18,
                            categoryId=7,
                            accountId=3)
    leetcode = Transaction(trans_date=date(2022, 2, 17),
                           trans_payee='Leetcode',
                           trans_amount=35.00,
                           categoryId=7,
                           accountId=2)

    stubhub = Transaction(trans_date=date(2022, 1, 21),
                          trans_payee='Stubhub',
                          trans_amount=105.10,
                          categoryId=8,
                          accountId=4)
    netflix_one = Transaction(trans_date=date(2022, 1, 2),
                              trans_payee='Netflix',
                              trans_amount=9.99,
                              categoryId=8,
                              accountId=2)
    netflix_two = Transaction(trans_date=date(2021, 12, 2),
                              trans_payee='Netflix',
                              trans_amount=9.99,
                              categoryId=8,
                              accountId=2)
    netflix_three = Transaction(trans_date=date(2021, 11, 2),
                                trans_payee='Netflix',
                                trans_amount=9.99,
                                categoryId=8,
                                accountId=2)
    netflix_four = Transaction(trans_date=date(2022, 2, 2),
                               trans_payee='Netflix',
                               trans_amount=9.99,
                               categoryId=8,
                               accountId=2)
    epic_games = Transaction(trans_date=date(2022, 2, 9),
                             trans_payee='Epic Games',
                             trans_amount=39.99,
                             categoryId=8,
                             accountId=2)
    netflix_five = Transaction(trans_date=date(2022, 3, 2),
                               trans_payee='Netflix',
                               trans_amount=9.99,
                               categoryId=8,
                               accountId=2)
    steam = Transaction(trans_date=date(2022, 3, 14),
                        trans_payee='Steam',
                        trans_amount=59.99,
                        categoryId=8,
                        accountId=4)
    netflix_six = Transaction(trans_date=date(2022, 4, 2),
                              trans_payee='Netflix',
                              trans_amount=9.99,
                              categoryId=8,
                              accountId=2)

    west_elm = Transaction(trans_date=date(2022, 1, 19),
                           trans_payee='West Elm',
                           trans_amount=81.21,
                           categoryId=15,
                           accountId=2)
    home_depot = Transaction(trans_date=date(2021, 12, 16),
                             trans_payee='Home Depot',
                             trans_amount=78.04,
                             categoryId=15,
                             accountId=4)
    west_buena = Transaction(trans_date=date(2022, 3, 10),
                             trans_payee='West Buena',
                             trans_amount=68.75,
                             categoryId=15,
                             accountId=3)

    db.session.add(philz_one)
    db.session.add(philz_two)
    db.session.add(philz_three)
    db.session.add(philz_four)
    db.session.add(starbucks)
    db.session.add(starbucks_two)
    db.session.add(bevmo)
    db.session.add(starbucks_three)
    db.session.add(philz_five)
    db.session.add(boba)
    db.session.add(starbucks_four)
    db.session.add(philz_six)
    db.session.add(starbucks_five)
    db.session.add(tonga)
    db.session.add(philz_seven)
    db.session.add(starbucks_six)

    db.session.add(chipotle_one)
    db.session.add(chipotle_two)
    db.session.add(chipotle_three)
    db.session.add(shake_shack)
    db.session.add(bojangles)
    db.session.add(buffalo)
    db.session.add(chipotle_four)
    db.session.add(chipotle_five)
    db.session.add(portillos)
    db.session.add(inNOut)
    db.session.add(chipotle_six)
    db.session.add(shake_shack_two)
    db.session.add(portillos_two)
    db.session.add(chipotle_seven)
    db.session.add(portillos_three)

    db.session.add(trader_joes)
    db.session.add(whole_foods)
    db.session.add(whole_foods_two)
    db.session.add(costco)
    db.session.add(trader_joes_two)
    db.session.add(costco_two)
    db.session.add(whole_foods_three)
    db.session.add(costco_three)
    db.session.add(trader_joes_three)

    db.session.add(chewy_one)
    db.session.add(chewy_two)
    db.session.add(chewy_three)
    db.session.add(chewy_four)
    db.session.add(chewy_five)

    db.session.add(amazon_one)
    db.session.add(amazon_two)
    db.session.add(amazon_three)
    db.session.add(taylor_stitch)
    db.session.add(drop)
    db.session.add(grailed)
    db.session.add(everlane)
    db.session.add(uniqlo)
    db.session.add(uniqlo_two)
    db.session.add(danner)
    db.session.add(keychron)
    db.session.add(pistol)
    db.session.add(amazon_four)
    db.session.add(amazon_five)
    db.session.add(rogue_territory)
    db.session.add(taylor_stitch_two)
    db.session.add(amazon_six)

    db.session.add(uber)
    db.session.add(uber_two)
    db.session.add(lyft)
    db.session.add(lyft_two)
    db.session.add(uber_three)
    db.session.add(lyft_three)

    db.session.add(udemy_one)
    db.session.add(udemy_two)
    db.session.add(leetcode)

    db.session.add(stubhub)
    db.session.add(netflix_one)
    db.session.add(netflix_two)
    db.session.add(netflix_three)
    db.session.add(netflix_four)
    db.session.add(epic_games)
    db.session.add(netflix_five)
    db.session.add(steam)
    db.session.add(netflix_six)

    db.session.add(west_elm)
    db.session.add(home_depot)
    db.session.add(west_buena)

    db.session.commit()


def undo_transactions():
    db.session.execute('TRUNCATE transactions RESTART IDENTITY CASCADE;')
    db.session.commit()
