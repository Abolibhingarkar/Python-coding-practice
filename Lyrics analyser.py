text = """Please picture me
In the trees
I hit my peak at seven feet
In the swing
Over the creek
I was too scared to jump in
But I, I was high in the sky
With Pennsylvania under me
Are there still beautiful things?
Sweet tea in the summer
Cross your heart, won't tell no other
And though I can't recall your face
I still got love for you
Your braids like a pattern
Love you to the moon and to Saturn
Passed down like folk songs
The love lasts so long
And I've been meaning to tell you
I think your house is haunted
Your dad is always mad and that must be why
And I think you should come live with
Me and we can be pirates
Then you won't have to cry
Or hide in the closet
And just like a folk song
Our love will be passed on
Please picture me
In the weeds
Before I learned civility
I used to scream ferociously
Any time I wanted
I, I
Sweet tea in the summer
Cross my heart, won't tell no other
And though I can't recall your face
I still got love for you
Pack your dolls and a sweater
We'll move to India forever
Passed down like folk songs
Our love lasts so long"""

print (text.split())
dictionary = {}

for letter in text.split():
    if letter in dictionary:
        dictionary[letter] += 1  
    else:
        dictionary[letter] = 1
    print (dictionary)