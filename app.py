import random
from flask import Flask, jsonify

app = Flask(__name__)

verses = [
    "For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life. - John 3:16",
    "Trust in the Lord with all your heart, and lean not on your own understanding; in all your ways acknowledge Him, and He will make your paths straight. - Proverbs 3:5-6",
    "I can do all things through Christ who strengthens me. - Philippians 4:13",
    "Be strong and courageous. Do not be afraid or terrified because of them, for the Lord your God goes with you; he will never leave you nor forsake you. - Deuteronomy 31:6",
    "The Lord is my shepherd, I lack nothing. He makes me lie down in green pastures, he leads me beside quiet waters, he refreshes my soul. - Psalm 23:1-3",
    "In the world you will have tribulation. But take heart; I have overcome the world.- John 16:33",
    "So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand.-Isaiah 41:10 (NIV)", 
    "Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God. And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.-Philippians 4:6–7 (NIV)",
    "I sought the LORD, and He answered me and delivered me from all my fears. Those who look to Him are radiant, and their faces shall never be ashamed. Oh, taste and see that the LORD is good! Blessed is the man who takes refuge in Him! - Psalm 34:4–5, 8",
    "And we know that for those who love God all things work together for good, for those who are called according to His purpose.- Romans 8:28",
    "Have I not commanded you? Be strong and courageous. Do not be frightened, and do not be dismayed, for the LORD your God is with you wherever you go.-Joshua 1:9",
    "So do not worry, saying, 'What shall we eat?' or 'What shall we drink?' or 'What shall we wear?' For the pagans run after all these things, and your heavenly Father knows that you need them. But seek first His kingdom and His righteousness, and all these things will be given to you as well. Therefore do not worry about tomorrow, for tomorrow will worry about itself. Each day has enough trouble of its own.-Matthew 6:31–34 (NIV)",
    "Trust in the LORD with all your heart, and do not lean on your own understanding. In all your ways acknowledge Him, and He will make straight your paths.-Proverbs 3:5–6",
    "May the God of hope fill you with all joy and peace as you trust in Him, so that you may overflow with hope by the power of the Holy Spirit.-Romans 15:13 (NIV)",
    "If my people who are called by My name humble themselves, and pray and seek My face and turn from their wicked ways, then I will hear from heaven and will forgive their sin and heal their land.-2 Chronicles 7:14",
    "Do nothing from selfish ambition or conceit, but in humility count others more significant than yourselves. Let each of you look not only to his own interests, but also to the interests of others.-Philippians 2:3–4",
    "For I, the LORD your God, hold your right hand; it is I who say to you, 'Fear not, I am the one who helps you.'-Isaiah 41:13",
    "Humble yourselves, therefore, under the mighty hand of God so that at the proper time He may exalt you, casting all your anxieties on Him, because He cares for you.-1 Peter 5:6–7",
    "When I thought, 'My foot slips,' Your steadfast love, O LORD, helped me up. When the cares of my heart are many, Your consolations cheer my soul.-Psalm 94:18–19",
    "He will wipe away every tear from their eyes, and death shall be no more, neither shall there be mourning, nor crying, nor pain anymore, for the former things have passed away. And He who was seated on the throne said, 'Behold, I am making all things new.'-Revelation 21:4"
]

@app.route('/')
def random_verse():
    verse = random.choice(verses)
    return jsonify({'verse': verse})

if __name__ == '__main__':
    app.run()

