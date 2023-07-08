-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Chceck the description of crime scence
SELECT description FROM crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28 AND street = 'Humphrey Street';
--Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.

-- Check the interviews
SELECT name, transcript FROM interviews
WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE '%bakery%';
--Ruth    | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.
--Eugene  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
--Raymond | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket.

-- Check the ATM
SELECT account_number
FROM atm_transactions
WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';
--+----------------+
--| account_number |
--+----------------+
--| 28500762       |
--| 28296815       |
--| 76054385       |
--| 49610011       |
--| 16153065       |
--| 25506511       |
--| 81061156       |
--| 26013199       |
--+----------------+

--Check bakery security logs
SELECT hour, minute, activity, license_plate
FROM bakery_security_logs
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25;

--+------+--------+----------+---------------+
--| hour | minute | activity | license_plate |
--+------+--------+----------+---------------+
--| 10   | 16     | exit     | 5P2BI95       |
--| 10   | 18     | exit     | 94KL13X       |
--| 10   | 18     | exit     | 6P58WS2       |
--| 10   | 19     | exit     | 4328GD8       |
--| 10   | 20     | exit     | G412CB7       |
--| 10   | 21     | exit     | L93JTIZ       |
--| 10   | 23     | exit     | 322W7JE       |
--| 10   | 23     | exit     | 0NTHK55       |
--+------+--------+----------+---------------+

--Check phone calls
SELECT caller, receiver
FROM phone_calls
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;
--+----------------+----------------+
--|     caller     |    receiver    |
--+----------------+----------------+
--| (130) 555-0289 | (996) 555-8899 |
--| (499) 555-9472 | (892) 555-8872 |
--| (367) 555-5533 | (375) 555-8161 |
--| (499) 555-9472 | (717) 555-1342 |
--| (286) 555-6063 | (676) 555-6554 |
--| (770) 555-1861 | (725) 555-3243 |
--| (031) 555-6622 | (910) 555-3251 |
--| (826) 555-1652 | (066) 555-9701 |
--| (338) 555-6650 | (704) 555-2131 |
--+----------------+----------------+

-- Check the destination
SELECT abbreviation, full_name, city
FROM airports, flights
WHERE airports.id = flights.destination_airport_id AND year = 2021 AND month = 7 AND day = 29 AND origin_airport_id =
(
    SELECT id
    FROM airports
    WHERE city = 'Fiftyville'
)
ORDER BY hour, minute
LIMIT 1;
--+--------------+-------------------+---------------+
--| abbreviation |     full_name     |     city      |
--+--------------+-------------------+---------------+
--| LGA          | LaGuardia Airport | New York City |
--+--------------+-------------------+---------------+

-- Passport numbers of all passengers flying first plane from 29th
SELECT passport_number
FROM passengers
WHERE flight_id =
(
    SELECT flights.id
    FROM airports, flights
    WHERE airports.id = flights.destination_airport_id AND year = 2021 AND month = 7 AND day = 29 AND origin_airport_id =
    (
        SELECT id
        FROM airports
        WHERE city = 'Fiftyville'
    )
    ORDER BY hour, minute
    LIMIT 1
);
--+-----------------+
--| passport_number |
--+-----------------+
--| 7214083635      |
--| 1695452385      |
--| 5773159633      |
--| 1540955065      |
--| 8294398571      |
--| 1988161715      |
--| 9878712108      |
--| 8496433585      |
--+-----------------+

-- Check who was withdrawing money
SELECT person_id
FROM bank_accounts
WHERE account_number IN
(
    SELECT account_number
    FROM atm_transactions
    WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'
);
--+-----------+
--| person_id |
--+-----------+
--| 686048    |
--| 514354    |
--| 458378    |
--| 395717    |
--| 396669    |
--| 467400    |
--| 449774    |
--| 438727    |
--+-----------+
SELECT name
FROM people
WHERE phone_number IN
(
    SELECT caller
    FROM phone_calls
    WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60
)
AND license_plate IN
(
    SELECT license_plate
    FROM bakery_security_logs
    WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25
)
AND passport_number IN
(
    SELECT passport_number
    FROM passengers
    WHERE flight_id =
    (
        SELECT flights.id
        FROM airports, flights
        WHERE airports.id = flights.destination_airport_id AND year = 2021 AND month = 7 AND day = 29 AND origin_airport_id =
        (
            SELECT id
            FROM airports
            WHERE city = 'Fiftyville'
        )
        ORDER BY hour, minute
        LIMIT 1
    )
)
AND id IN
(
    SELECT person_id
    FROM bank_accounts
    WHERE account_number IN
    (
        SELECT account_number
        FROM atm_transactions
        WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'
    )
);
--+-------+
--| name  |
--+-------+
--| Bruce |
--+-------+

SELECT name
FROM people
WHERE phone_number IN
(
    SELECT receiver
    FROM phone_calls
    WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60 AND caller IN
    (
        SELECT phone_number
        FROM people
        WHERE name =
        (
            SELECT name
            FROM people
            WHERE phone_number IN
            (
                SELECT caller
                FROM phone_calls
                WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60
            )
            AND license_plate IN
            (
                SELECT license_plate
                FROM bakery_security_logs
                WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25
            )
            AND passport_number IN
            (
                SELECT passport_number
                FROM passengers
                WHERE flight_id =
                (
                    SELECT flights.id
                    FROM airports, flights
                    WHERE airports.id = flights.destination_airport_id AND year = 2021 AND month = 7 AND day = 29 AND origin_airport_id =
                    (
                        SELECT id
                        FROM airports
                        WHERE city = 'Fiftyville'
                    )
                    ORDER BY hour, minute
                    LIMIT 1
                )
            )
            AND id IN
            (
                SELECT person_id
                FROM bank_accounts
                WHERE account_number IN
                (
                    SELECT account_number
                    FROM atm_transactions
                    WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'
                )
            )
        )
    )
);
--+-------+
--| name  |
--+-------+
--| Robin |
--+-------+
