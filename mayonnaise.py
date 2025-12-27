import random;t = random.randint(0, 9);s = list("mayonnaise");s[t] =  chr(ord(s[t]) - ord('a') + ord('A'));print("".join(s));
