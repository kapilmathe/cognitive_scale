# Cognitive Scale: Bank web Service
> Specification for REST API endpoing
-   Create user (create_user)
    -   required information:
        > username.

        > password.

        > email_address.

    -   workflow for creating user:
        > accept information and validate input received.

        > create user entry in user database with verification_status as False. generate token with expirition.

        > send email for verification with confimation link build using token.

        > send api response stating:
          - User created (please verify the email) with (ok :200)*.
          - If any exception occur: send appropriate failure message.


-   Get Balance info & Transaction Summary
    -   required information:
        > user_id

    -   workflow for getting balance and tx summary:
        > if user authenticated:

            > use user_id to get balance.
            > use user_id to get last 10 transaction
            > send acquired information (json serialized)  as api response.

        > if user not authenticated or any exception:

            > send out appropriate failure response


-   Add Beneficiary
    -   required information
        > beneficiary name

        > beneficiary account number

        > beneficiary nickname

        > bank name (if Other Bank)

        > bank branch code (IFSC code)

    -   workflow:
        > create beneficiary record in user_beneficiary collection.

        > send response: Success if no exception else  Failed

-   Delete Beneficiary
    -   required information:
        > beneficiary_id

    -   workflow:
        > remove record correspond to beneficiary from user_beneficiary collection

        > send responseL: Success if no exception else Failed

-   Transfer funds instant and schedule for given date and time
    -   Assumptions:
        > fund amount validation already completed at client app side(for instant transfer)

    -   required information:
        > beneficiary_id

        > amount

        > schedule (optional)

    -   workflow:
        > if schedule mentioned: create schedule transfer record in schedule_transaction colletion with received informations

        > instant transfer:

            > same bank: debit amount from user account.
            > same bank: creadit amount in beneficiary account for calling deposit api endpoing with beneficairy account number and amount.
            > same bank: if both the operation successful return Success response code otherwise ROLLLBACK transactions.

            > other bank: debit amount from user account:
            > other bank: credit amound in beneficiary account for calling deposit api endpoint of corresponding bank api with required information.
            > other bank: if both the operation successful return Success response code otherwise ROLLLBACK transactions.

-   Calculate balance for user account for future date, given base interest rate of 4%
    -   Assumption:
        > next 6 years prediction

    -   required information:
        > current balance

    -   workflow:
        > calculate future balance for 6 months
        > send response in json serialized format





