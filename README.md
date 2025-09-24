# Cerberus
Cerberus is a thread-manager that is able to run different files, with a frequency.

### targets.json
```
 [
     {
       "name": "Test script!",
       "target": "/home/user/Coding/calculate_pi.py",
       "frequency": 10,
       "SHOW_OUTPUT": false
     }
 ]
```
- **name**, the name of the thread, for error handeling and reusability
- **target**, target file name
- **frequency**, the frequency of delay after re-running the script in seconds
- **SHOW_OUTPUT**, show the output of the target file in current console 
