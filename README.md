
# python-password-generator
A secure and modern GUI-based Random Password Generator built using Python and Tkinter.
# Simple GUI Password Generator 🔑

Hi everyone! Maine practicing ke liye Python ka use karke ek chhota sa desktop app banaya hai. Aaj kal weak passwords ki wajah se accounts jaldi hack ho jaate hain, isiliye maine ek aisa tool banaya hai jo ek click me ekdum strong aur random password bana deta hai.

Pehle maine iska ek basic black-and-white terminal version banaya tha, par dekhne me thoda boring lag raha tha. Isiliye maine Tkinter use karke isme ek badhiya sa dark mode interface (GUI) add kar diya hai taaki koi bhi ise aasaani se chalaye aur dekhne me bhi cool lage.

---

## 🔥 Isko Chalane Ka Tarika (Run Commands)

Ise run karna bahut simple hai, bas ye steps follow karein:

1. Sabse pehle apne computer me Terminal ya Command Prompt khol lein.
2. `cd` command ka use karke us folder ke andar chale jayein jahan aapki `pass.py` file saved hai. Jaise agar desktop par hai toh:

```bash
cd Desktop/my-project
```

3. Ab bas ye command likh kar enter daba edin:

- **Windows par:**
```bash
python pass.py
```

- **Mac ya Linux par:**
```bash
python3 pass.py
```

---

## 🛠️ Maine Isme Kya-Kya Features Dale Hain?

- **Dark Mode UI:** Iska background maine dark rakha hai taaki screen par dekhne me aakhon par zor na pade.
- **Length Slider:** Aap slider ko aage-pichhe karke khud decide kar sakte hain ki aapko kitne characters bada password chahiye (6 se lekar 32 tak).
- **Custom Options:** Teen checkboxes hain jisse aap khud choose kar sakte hain ki password me sirf letters hon, numbers hon, ya special characters (jaise @, #, \$) bhi shamil karne hain.
- **Copy Button:** Password generate hone ke baad bar-bar select karke copy karne ka jhanjhat nahi hai. Bas "Copy" button par click karo aur password aapke phone/laptop me direct copy ho jayega.
- **Smart Warnings:** Agar aap teeno checkboxes ko uncheck (khali) karke button daba doge, toh application gussa nahi karega balki ek pop-up warning dikha dega ki "bhai, kam se kam ek option toh select karo!".

---

## 🧠 Yeh Kaam Kaise Karta Hai?

<img width="1016" height="550" alt="Screenshot_2026-09-21_23_33_57" src="https://github.com/user-attachments/assets/033e258e-defc-4bb8-8ae3-1c14e15f1779" />

Maine isme Python ke do inbuilt modules use kiye hain—`random` aur `string`. 
Jab aap button dabate hain, toh program aapke select kiye gaye options (letters, numbers, symbols) ko ek badi list me mila deta hai. Phir computer bina kisi insani dimag ke, completely random tarike se har position ke liye alag character uthata hai aur unhe jodkar ek solid password screen par display kar deta hai.
kar deta hai.
r aapki select ki hui length ke hisab se alag-alag letters aur symbols ko aapas me mix karke ek solid output screen par show kar deta hai.
