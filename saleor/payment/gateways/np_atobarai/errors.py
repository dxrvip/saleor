from enum import Enum
from typing import Iterable, List


class NPAtobaraiError(Exception):
    pass


class TransactionRegistrationResultError(Enum):
    # Customer name (Kanji)
    E0100048 = "Please make sure that the your (Kanji) has been entered."
    E0100049 = (
        "Please confirm that your name(Kanji) does not include prohibited characters."
    )
    E0100050 = (
        "Please confirm that your name(Kanji) is within 21 full - width characters."
    )

    # Customer name (Kana)
    E0100051 = (
        "Please confirm that your name(Kana) is within 25 full - width characters."
    )
    E0100052 = (
        "Please confirm that your name(kana) does not contain prohibited characters."
    )

    # Customer's company name
    E0100053 = (
        "Please confirm that your company name is within 30 full - width characters."
    )
    E0100054 = (
        "Please confirm that your company name does not include prohibited characters."
    )

    # Customer's department name
    E0100055 = (
        "Please confirm that your department name is within 30 full - width characters."
    )
    E0100056 = (
        "Please confirm that your department name "
        "does not include prohibited characters."
    )

    # Customer's ZIP code
    E0100057 = "Please check if the customer’s ZIP code has been entered."
    E0100058 = (
        "Please confirm that the customer’s ZIP code "
        "does not contain prohibited characters."
    )
    E0100136 = (
        "Please check if the customer’s ZIP code "
        "format is correct.(Example: 1070052, 107 - 0052)"
    )
    E0100059 = "Please check if the customer’s ZIP code and address match."

    # Customer's address
    E0100060 = "Please make sure that the customer’s address has been entered."
    E0100061 = (
        "Please make sure that the customer’s address "
        "does not contain prohibited characters."
    )
    E0100062 = (
        "Please make sure that the Customer’s address "
        "is within 55 full - width characters."
    )

    # Customer's phone number
    E0100063 = "Please check if the customer’s phone number has been entered."
    E0100064 = (
        "Please confirm that the customer’s phone number "
        "does not contain prohibited characters."
    )
    E0100065 = "Please confirm that the formant of the phone number is valid."
    E0100066 = (
        "If the first to third digits of the phone number excluding the hyphen are "
        "“020”, “050”, “060”, “070”, “0 80”, or “0 90”, please ensure that "
        "the phone number has 11 digits."
    )
    E0100067 = (
        "If the first to third digits of the phone number excluding the hyphen "
        "are other than the above, please check if it has 10 digits."
    )

    # Customer's email address
    E0100068 = "This item is required by merchants."
    E0100069 = (
        "Please confirm that the customer’s email address "
        "does not contain prohibited characters."
    )
    E0100070 = (
        "Please check if the Customer’s email address is within 100 ASCII characters."
    )
    E0100071 = "Please confirm that the formant of the email address is valid."

    # Delivery destination (Kanji)
    E0100072 = "Please check if the delivery destination (Kanji) has been entered."
    E0100073 = (
        "Please make sure that the delivery destination (Kanji) "
        "does not contain prohibited characters."
    )
    E0100074 = (
        "Please confirm that the delivery destination (Kanji) "
        "is within 21 full-width characters."
    )

    # Delivery destination (Kana)
    E0100075 = (
        "Please confirm that the delivery destination (Kana) "
        "is within 25 full-width characters."
    )
    E0100076 = (
        "Please make sure that the delivery destination (Kana) "
        "does not contain prohibited characters."
    )

    # Delivery destination (company name)
    E0100077 = (
        "Please confirm that the delivery destination (company name) "
        "is within 30 full-width characters."
    )
    E0100078 = (
        "Please confirm that the delivery destination (company name) "
        "does not include prohibited characters."
    )

    # Delivery destination (department name)
    E0100079 = (
        "Please confirm that the delivery destination (department name) "
        "is entered within 30 full-width characters."
    )
    E0100080 = (
        "Please confirm that the delivery destination (department name) "
        "does not contain prohibited characters."
    )

    # Delivery destination (ZIP code)
    E0100081 = "Please check if the delivery destination(ZIP code) has been entered."
    E0100082 = (
        "Please make sure that the delivery destination(ZIP code) "
        "does not contain prohibited characters."
    )
    E0100137 = (
        "Please check if the delivery destination(ZIP code) "
        "is in the correct format.(Example: 1070052, 107 - 0052)"
    )
    E0100083 = "Please make sure the delivery destination (ZIP code) and address match."

    # Delivery destination (address)
    E0100084 = "Please check if the delivery destination(address) has been entered."
    E0100085 = (
        "Please make sure that the delivery destination(address) "
        "does not contain prohibited characters."
    )
    E0100086 = (
        "Please confirm that the delivery destination(address) "
        "is within 55 full - width characters."
    )

    # Delivery destination (phone number)
    E0100087 = (
        "Please check if the delivery destination(phone number) has been entered."
    )
    E0100088 = (
        "Please make sure that the delivery destination(phone number) "
        "does not contain prohibited characters."
    )
    E0100089 = "Please ensure the phone number format is valid."
    E0100090 = (
        "If the 1 st to 3 rd digit of the phone number excluding the hyphen is "
        "“020”, “050”, “060”, “070”, “0 80”, or “0 90”, please ensure "
        "that the phone number has a total of 11 digits."
    )
    E0100091 = "Please check if the delivery phone number is entered."


class PendingReason(Enum):
    RE009 = (
        "Please check your registered address, "
        "as there may be insufficient address information."
        "(1. Please enter the name of the building or room number. "
        "2. Please enter the name of the company or store in the “Company Name” box.)"
    )

    RE014 = (
        "NP atobarai cannot be used for deliveries to temporary destinations "
        "(hotels, etc.) or for picking up items at post offices, convenience stores, "
        "or shipping company offices.Please check your registered address "
        "and the enrollment status of the purchaser in provided address. "
        "Please contact the NP Support Desk if you are eligible to use NP atobarai, "
        "for example, if you are a staff member."
    )

    RE015 = (
        "Please check your registered shipping address, "
        "as the address information may be insufficient. "
        "(1. Please enter the name of the building or room number. "
        "2. Please enter the name of the company or store in the “Company Name” field.)"
    )

    RE020 = (
        "NP atobarai is not available for deliveries to temporary destinations "
        "(hotels, etc.) or for picking up items at post offices, convenience stores, "
        "or shipping company offices. Please check your registered address "
        "and the enrollment status of the purchaser in provided address. "
        "Please contact the NP Support Desk if it is available to use NP atobarai "
        "such as order by stuff member."
    )

    RE021 = (
        "Provided phone number has something wrong and it caused an error. "
        "Please update your phone number."
    )

    RE023 = (
        "Provided phone number for the shipping address has something wrong "
        "and it caused an error. Please update your phone number."
    )

    RE026 = (
        "If the registered address is to P.O. Box, if you are an employee of the "
        "merchant (in-house transactions), if the website is not examined yet, "
        "if you only charge shipping and handling fee, if you sell prohibited products "
        "(including digital content, animals, tickets, course fees, etc., which you "
        "have started selling after we have completed our review of the merchant), "
        "please cancel the transaction if it apply to any of the above."
    )


def get_reason_messages_from_codes(
    reason_codes: Iterable[str],
) -> List[str]:
    reason_messages = []
    for code in reason_codes:
        try:
            message = PendingReason[code].value
        except KeyError:
            # The number of pending codes may increase in the future.
            message = f"#{code}: {UNKNOWN_REASON}"

        reason_messages.append(message)

    return reason_messages


UNKNOWN_ERROR = "Unknown error while processing the payment."

UNKNOWN_REASON = "Unknown pending reason while processing the payment."
