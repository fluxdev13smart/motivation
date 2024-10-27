import discord
import random

# Replace with your bot's token
TOKEN = 'MTIyMTM4NDEwMDkwNTIyMjIwNQ.G8wZLs.CZvK5O49-f-cKsfSzUf_nE0682SXkKhUADMNak'

# Extended list of motivational quotes
quotes = [
    "Believe in yourself!",
    "You can do it!",
    "Every day is a second chance.",
    "Stay positive, work hard, make it happen.",
    "Don't watch the clock; do what it does. Keep going.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The way to get started is to quit talking and begin doing.",
    "Keep your eyes on the stars and your feet on the ground.",
    "It always seems impossible until it’s done.",
    "Success is the sum of small efforts, repeated day in and day out.",
    "Act as if what you do makes a difference. It does.",
    "You don’t have to be great to start, but you have to start to be great.",
    "Dream big and dare to fail.",
    "Don’t wait for the perfect moment. Take the moment and make it perfect.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Don’t be afraid to give up the good to go for the great.",
    "Great things never come from comfort zones.",
    "Little by little, one travels far.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Your limitation—it’s only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Sometimes later becomes never. Do it now.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The key to success is to focus on goals, not obstacles.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Do something today that your future self will thank you for.",
    "It’s going to be hard, but hard does not mean impossible.",
    "Don’t wait for opportunity. Create it.",
    "Small progress is still progress.",
    "Failure is not the opposite of success; it’s part of success.",
    "What defines us is how well we rise after falling.",
    "Difficult roads often lead to beautiful destinations.",
    "Don’t quit. Suffer now and live the rest of your life as a champion.",
    "Success is what happens after you have survived all of your mistakes.",
    "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart.",
    "You are stronger than you think.",
    "Strength doesn’t come from what you can do. It comes from overcoming the things you once thought you couldn’t.",
    "You don’t have to be perfect to be amazing.",
    "Your mind is a powerful thing. When you fill it with positive thoughts, your life will start to change.",
    "You only fail when you stop trying.",
    "Make today so awesome, yesterday gets jealous.",
    "Don’t tell people your plans. Show them your results.",
    "If you can dream it, you can do it.",
    "Your attitude, not your aptitude, will determine your altitude.",
    "Hardships often prepare ordinary people for an extraordinary destiny.",
    "You’re allowed to scream, you’re allowed to cry, but do not give up.",
    "What we achieve inwardly will change outer reality.",
    "Every accomplishment starts with the decision to try.",
    "You miss 100% of the shots you don’t take.",
    "The best way to predict the future is to create it.",
    "Opportunities don’t happen, you create them.",
    "Don’t limit your challenges. Challenge your limits.",
    "Start where you are. Use what you have. Do what you can.",
    "Success is liking yourself, liking what you do, and liking how you do it.",
    "There is no elevator to success. You have to take the stairs.",
    "The only place where success comes before work is in the dictionary.",
    "Success isn’t about how much money you make; it’s about the difference you make in people’s lives.",
    "I never dreamed about success. I worked for it.",
    "Be so good they can’t ignore you.",
    "What would you do if you weren’t afraid?",
    "Act as if it were impossible to fail.",
    "Turn your wounds into wisdom.",
    "Don’t compare your beginning to someone else’s middle.",
    "The biggest adventure you can take is to live the life of your dreams.",
    "You don’t have to see the whole staircase, just take the first step.",
    "Everything you’ve ever wanted is on the other side of fear.",
    "Go confidently in the direction of your dreams. Live the life you’ve imagined.",
    "Success is not the key to happiness. Happiness is the key to success.",
    "Failure will never overtake me if my determination to succeed is strong enough.",
    "Your life only gets better when you get better.",
    "Stay close to anything that makes you glad you’re alive.",
    "We generate fears while we sit. We overcome them by action.",
    "Success usually comes to those who are too busy to be looking for it.",
    "The only difference between success and failure is the ability to take action.",
    "When you want to succeed as bad as you want to breathe, then you’ll be successful.",
    "It’s not whether you get knocked down, it’s whether you get up.",
    "There are no secrets to success. It is the result of preparation, hard work, and learning from failure.",
    "The successful warrior is the average man, with laser-like focus.",
    "Motivation is what gets you started. Habit is what keeps you going.",
    "The harder the battle, the sweeter the victory.",
    "Winners are not people who never fail, but people who never quit.",
    "If it doesn’t challenge you, it won’t change you.",
    "Success is nothing more than a few simple disciplines, practiced every day.",
    "Don’t wish it were easier; wish you were better.",
    "Believe you can and you’re halfway there.",
    "The pain you feel today will be the strength you feel tomorrow.",
    "A little progress each day adds up to big results.",
    "Challenges are what make life interesting. Overcoming them is what makes life meaningful.",
    "Success is the progressive realization of a worthy goal or ideal.",
    "When we strive to become better than we are, everything around us becomes better too.",
    "Aim for the moon. If you miss, you may hit a star.",
    "Your greatest asset is your earning ability. Your greatest resource is your time.",
    "Don’t be afraid to stand for what you believe in, even if that means standing alone.",
    "It does not matter how slowly you go, as long as you do not stop.",
    "The secret of getting ahead is getting started.",
    "Your dream doesn’t have an expiration date. Take a deep breath and try again.",
    "If you want to achieve greatness, stop asking for permission.",
    "It’s never too late to be what you might have been.",
    "The future depends on what you do today.",
    "A goal without a plan is just a wish.",
    "The only person you are destined to become is the person you decide to be.",
    "What you get by achieving your goals is not as important as what you become by achieving your goals.",
    "You will never always be motivated, so you must learn to be disciplined.",
    "Dreams don’t work unless you do.",
    "Success is not how high you have climbed, but how you make a positive difference to the world.",
    "Don’t let the fear of losing be greater than the excitement of winning.",
    "It’s not about having time. It’s about making time.",
    "Doubt kills more dreams than failure ever will.",
    "You are never too old to set another goal or to dream a new dream.",
    "Success is getting what you want. Happiness is wanting what you get.",
    "A comfort zone is a beautiful place, but nothing ever grows there.",
    "The expert in anything was once a beginner.",
    "Don’t stop when you’re tired; stop when you’re done.",
    "Life is short, and it is up to you to make it sweet.",
    "You can’t have a million-dollar dream with a minimum-wage work ethic.",
    "Success is stumbling from failure to failure with no loss of enthusiasm.",
    "You never know how strong you are, until being strong is your only choice.",
    "The only way to achieve the impossible is to believe it is possible.",
    "Hard times don’t create heroes. It is during the hard times when the ‘hero’ within us is revealed.",
    "If you are not willing to risk the usual, you will have to settle for the ordinary.",
    "There is only one thing that makes a dream impossible to achieve: the fear of failure."
]

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!motivate'):
        quote = random.choice(quotes)
        await message.channel.send(quote)

client.run(TOKEN)
