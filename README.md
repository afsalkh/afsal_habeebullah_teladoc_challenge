# afsal_habeebullah_teladoc_challenge
Basic selenium automation for teladoc discussion




## Running Tests

To run tests, navigate to Tests folder

```cd Tests```

Run all tests using
```bash
  pytest -s --browser=chrome -v
```
<br/><br/>
Run the tests with matching markers
```bash
  pytest -s -m markername --browser=chrome -v
```
Currently available markers are: ```addgroup, deletegroup```
<br/><br/>

Run specific tests using
```bash
  pytest -s -k test_name --browser=chrome -v
```
<br/><br/>
--browser by default is chrome. Supported values are ```chrome, edge```

## Support
For support, email afsalkh@gmail.com


