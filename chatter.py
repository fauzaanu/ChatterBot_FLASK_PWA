from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, UbuntuCorpusTrainer, ListTrainer


# The only required parameter for the ChatBot is a name. This can be anything you want.
chatbot = ChatBot("Sage", 
    logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'syntax to train: question|response',
                'maximum_similarity_threshold': 0.10
            },
        ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ]
    )





def asksage(question):

    # if the question is a training question
    if question.find("|") != -1:
        # split the question into question and response
        question, response = question.split("|")


        # train the chatbot with the question and response
        trainer = ListTrainer(chatbot)
        trainer.train([
            str(question),
            str(response)
        ])
    

    # Get a response to an input statement
    response = chatbot.get_response(question)

    print(response)

    return str(response)



if __name__ == '__main__':

    # train sage with the ubunu corpus
    trainer =  UbuntuCorpusTrainer(chatbot)

    # make sure to get verbose output while training
    trainer.train()


    while True:
        try:
            x = input()
            if len(x.split("|")) == 2:
                print(len(x.split("|")))
                y = x.split("|")
                # training
                conversation = [
                    str(y[0]),
                    str(y[1]),
                ]
                print(y)

                trainer = ListTrainer(chatbot)
                trainer.train(conversation)
            else:
                bot_input = chatbot.get_response(x)
                print(bot_input)

        except(KeyboardInterrupt, EOFError, SystemExit):
            break