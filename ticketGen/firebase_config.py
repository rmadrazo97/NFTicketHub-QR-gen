import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("credentials/nftickethub-firebase-adminsdk-yjler-d6bb053362.json")
firebase_app = firebase_admin.initialize_app(cred, {
    "storageBucket": "nftickethub.appspot.com",
    "databaseURL": "https://nftickethub-default-rtdb.europe-west1.firebasedatabase.app/"
})
