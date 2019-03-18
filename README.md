# Comics publisher

This App helps you to post random comics from xckd to your VK public.

### How to install

1. You need to [create VK App](https://vk.com/apps?act=manage). Choose Standalone type of app.
2. Get access token using [Implicit flow](https://vk.com/dev/implicit_flow_user). In scope parameter use: photos,groups,wall,offline
3. Create .env file and add access_token=your_token from Step 2
4. Install dependencies (written below)

Note: Comics download from [xckd docs](https://xkcd.com/json.html)

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### Program output example
```
python main.py
>> Запись успешно добавлена!
```
Note: after that in your VK public a record will appear
<img src="https://i.ibb.co/0JBSFqK/comics.png" alt="comics" border="0">

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).