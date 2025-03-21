In a distributed system, network communication among the numerous components can fail anytime. Client applications deal with these failures by implementing retries. Let's assume that we have a client application that invokes the remote service – "shaky_service". The client application must retry, in case the shaky_service returns False or None. 

However, the client applications must implement retries responsibly. Calling  again, without waiting, may overwhelm the system, and contribute to further degradation of the service that is already under distress. Exponential backoff is a common strategy for handling retries of failed network calls. In simple terms, the clients wait progressively longer intervals between consecutive retries.

Start with completing the implementation of the backoff decorator below:

    from random import randint
    from time import sleep, asctime


    def backoff(func: callable) -> callable:
        inital_delay = 0.01
        back_off_factor = 2
        delay = 0

        def inner(*args, **kwargs):
        ...


    @backoff
    def call_shaky_service():
        return 6 == randint(1, 6)


    while True:
        print(call_shaky_service())

Once you have it working and it outputs something like this ....

    Fri Dec 30 11:39:03 2022: will be calling call_shaky_service after 0 sec delay
    False
    Fri Dec 30 11:39:03 2022: will be calling call_shaky_service after 0.01 sec delay
    True
    Fri Dec 30 11:39:03 2022: will be calling call_shaky_service after None sec delay
    False
    Fri Dec 30 11:39:03 2022: will be calling call_shaky_service after 0.01 sec delay
    False
    Fri Dec 30 11:39:03 2022: will be calling call_shaky_service after 0.02 sec delay
    False
    Fri Dec 30 11:39:03 2022: will be calling call_shaky_service after 0.04 sec delay
    False
    Fri Dec 30 11:39:03 2022: will be calling call_shaky_service after 0.08 sec delay

.. improve the implementation by parameterizing the decorator, like you see it used below:

    @backoff(inital_delay=0.1, back_off_factor=1.5, max_delay=2.5)
    def call_shaky_service():
        return 6 == randint(1, 6)

The output might now look something like this:

    Fri Dec 30 12:22:22 2022: will be calling call_shaky_service after 0 sec delay
    False
    Fri Dec 30 12:22:22 2022: will be calling call_shaky_service after 0.1 sec delay
    True
    Fri Dec 30 12:22:22 2022: will be calling call_shaky_service after None sec delay
    True
    Fri Dec 30 12:22:22 2022: will be calling call_shaky_service after None sec delay
    False
    Fri Dec 30 12:22:22 2022: will be calling call_shaky_service after 0.1 sec delay
    False
    Fri Dec 30 12:22:22 2022: will be calling call_shaky_service after 0.15000000000000002 sec delay
    False
    Fri Dec 30 12:22:22 2022: will be calling call_shaky_service after 0.22500000000000003 sec delay
    False
    Fri Dec 30 12:22:23 2022: will be calling call_shaky_service after 0.3375 sec delay
    False
    Fri Dec 30 12:22:23 2022: will be calling call_shaky_service after 0.5062500000000001 sec delay
    False
    Fri Dec 30 12:22:24 2022: will be calling call_shaky_service after 0.7593750000000001 sec delay
    False
    Fri Dec 30 12:22:24 2022: will be calling call_shaky_service after 1.1390625 sec delay
    False
    Fri Dec 30 12:22:25 2022: will be calling call_shaky_service after 1.7085937500000001 sec delay
    False
    Fri Dec 30 12:22:27 2022: will be calling call_shaky_service after 2.5 sec delay
    False
    Fri Dec 30 12:22:30 2022: will be calling call_shaky_service after 2.5 sec delay

You only need to submit the improved / parameterizing version of your solution.