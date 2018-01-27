The Phishing Detection Chrome Extension aims to classify, every browsed URL, under phished and non-phished category(on page load); thereby, alerting the user of any malicious activity and prevent intrusion.

Steps to install the chrome extension:
1. Google Chrome -> More Tools -> Extensions
2. Click 'Load unpacked extension..'
3. Open the 'Engineering Module' directory
4. Phishing Detection extension ready to monitor all the sites loaded on the Chrome browser

Test URLs(positive tests - phishing detected):
1. ../Engineering Module/Phishing.html (Test phished page created)
2. https://www.phishtank.com/phish_search.php?verified=u&active=y (List of phished sites available)

ML Algorithms:
SVM, Neural Networks and Random Forest algorithms have been used to evaluate the data-set; and the SVM trained persistent model has been passed to the engineering module for phishing detection.

Engineering Modules:
1. manifest.json:
It provides Chrome with the basic information about the extension like name, permissions, associated scripts and files.

2. content.js:
It runs in separate unprivileged javscript environment and has complete access to the DOM.
Here, the trained SVM model(weights calculated in ./ML Algorithm Evaluation/run_algorithms.py) has been used as a persistent model to classify websites.
Below functions compute feature vector for the portal under analysis:
isIPInURL()
isLongURL()
isTinyURL()
isAlphaNumericURL()
isRedirectingURL()
isHypenURL()
isMultiDomainURL()
isFaviconDomainUnidentical()
isIllegalHttpsURL()
isImgFromDifferentDomain()
isAnchorFromDifferentDomain()
isScLnkFromDifferentDomain()
isFormActionInvalid()
isMailToAvailable()
isStatusBarTampered()
isIframePresent()
The evaluated feature vector, further, passed to predict(data) function reckons the prediction for the website.

3. background.js: 
In case, we need access to external extensions or APIs, it is a requisite to create means of communication between the content.js and privileged parts of the our extension, and this interaction is termed as message passing. Message passing allows different components of our extension to collabrate. 

NOTE: The extension validates every URL call, i.e. in case of URL redirection, it will assess every intermittent URL hit as well.

