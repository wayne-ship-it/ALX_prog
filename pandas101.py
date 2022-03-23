# using pandas
import pandas as pd
registration = {
    'cars': ['volkswagen', 'Mitsubishi', 'Toyota'],
    'plate No': ['UAW 465L', 'UBX 789O', 'UCB 344P']
}

myvar = pd.DataFrame(registration)

print(myvar, file=open('reg.txt', 'a'))

print('Panda version is ' + pd.__version__, file=open('reg.txt', 'a'))

# you can use the f.open and f.close function to the same but it also closes the file after the output is complete
f = open('output.txt', 'a')
print('my name is jurua evans wayne', file=f)
print('her name is Hinata', file=f)
f.close()
