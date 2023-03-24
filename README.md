# Elevator_System_New

LIST OF API END POINTS

1.) GET http://127.0.0.1:8000/api/v1/Elevators/ : fetches  the info of all the elevators in the system.

2.) POST http://127.0.0.1:8000/api/v1/Elevators/initialize : Inintialize the whole elevator with "n" input from user.

3.) GET http://127.0.0.1:8000/api/v1/Elevators/initialize : Fetch the info of "n" initialized elevator.

4.) GET  http://127.0.0.1:8000/api/v1/Elevators/{elevator_id}/next_destination: Fetches the next destination of a lift.

5.) GET  http://127.0.0.1:8000/api/v1/Elevators/{elevator_id}/get_direction : Fetches the dicrection of list (up,or down). 

6.) GET  http://127.0.0.1:8000/api/v1/Elevators/{elevator_id}/get_elevator_request_list : Fetches the list of request for an elevator.

7.) PATCH http://127.0.0.1:8000/api/v1/Elevators/{elevator_id}/getting_left_request : Update the current and destination of for a lift.

8.) GET http://127.0.0.1:8000/api/v1/Elevators/{elevator_id}/getting_left_request : Display the updated lift condition .
 
Screen recording Link:

https://drive.google.com/file/d/1QJ5Tzw01z3QT246gmDb-R3MQciTTBBD_/view?usp=share_link
