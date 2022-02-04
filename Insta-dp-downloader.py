#this a  small program :- automating  instagram profile images  download

#you can tweak this code to get your work done

#Instaloader is a tool to download pictures (or videos) along with their captions and other metadata from Instagram.
import instaloader

ig = instaloader.Instaloader()

#here you can attach your instagram profile name file.txt
#in this case i attached a sample file called insta_profiles.txt
f =  open('insta_profiles.txt') 

lines = f.readlines()
new_lines =[]

#this will remove the /n characters in the list
for line in lines:
    new_lines.append(line.strip())


for newline in new_lines:
    dp = newline
    print ()
    try:
        ig.download_profile(dp ,     profile_pic_only=True)
    except Exception:
        print (f"no profile named with {dp}")
        print ()

f.close()
