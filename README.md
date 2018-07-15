# Cognitive Scale: Bank web Service
> Specification for REST API endpoing
-   Create user account (create_account)
    -   Assumptions:
        > client already created bu "create_user" api call with proper username, password and email_id
        
    -   required information:
        > branch_code.

        > client_id.

        > initial_amount.

    -   workflow for creating user:
        > accept information and validate input received.

        > create account under provided branch and return account_number generated.

        > send api response stating:
          - Account created  with (CREATED :201)*.
          - If any exception occur: send appropriate failure message with status code (400 BAD REQUEST).


-   Get Balance info & Transaction Summary
    -   required information:
        > user_id
        
        > account_number 

    -   workflow for getting balance and tx summary:
        > if user authenticated:

            > use account_no to get balance.
            > use account_no to get last 10 transaction
            > send acquired information (json serialized)  as api response with status code (OK: 200).

        > if user not authenticated or any exception:

            > send out appropriate failure response


-   Add Beneficiary:
    -   Assumptions:
        > there is some way to validate the IFSC code in atual banking system, but here I used local bank list to validate it.
        
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
        > Major assumption for the scope of this iteration: Considering no concurrency race condtion
        
        > code simply implemented without handling Critical Section Problem
        
        > Possible solution uses following logic:
        
            > FIFO logic: first come first serve transaction request.
            
            > Using any message queue will suffice.
            
            > Higher traffic: 
            > Have multiple consumers(workers) which consume transaction request.
            > Have dedicated worker for high transaction rate account.  
                     
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





