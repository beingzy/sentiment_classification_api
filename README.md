## Sentiment Classification as Service
In this project, we deploy sentiment classification analysis as service via API. 

### Set up Restful API server
Change your current directory to the directory where `api.py` file reside, execute following command at terminal
```bash
python api.py
```

### API usage
In terminal, 
```bash
curl http://localhost:5000/sentiment/v0.1 -d "text='I am so excited to be able to use Pinterst everday to collect ideas from all over the world!'" -X PUT
```

In Python console,
```python
from requests import put, get 

endpoint_url = 'http://localhost:5000/sentiment/v0.1'
data_pkg = {'text': 'I am so excited to be able to use Pinterst everday to collect ideas from all over the world!'}

put(endpoint_url, data=data_pkg).json()
```

### Deploy to Heroku
Craete a heroku dyno, `heroku create`, and deploy the project, `git push heroku master`.
Attach logging service `heroku addons:create papertrail`. To check the logging, `heroku addons:open papertrail`.