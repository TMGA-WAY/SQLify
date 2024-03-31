import logging
import openai

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PromptCreation:
    @staticmethod
    def generic_prompt(client, messages):
        """
        This function create the prompt, request and return the response
        :param client: OpenAI client
        :param messages: Question of the user
        :return: Stream that contain the response
        """
        try:

            res = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": 'user', "content": PromptCreation.generate_prompt_with_context(messages)}])

            return res.choices[0].message.content

        except Exception as e:
            logger.info(f"Inside generic_prompt function.\n {e}")

    @staticmethod
    def generate_prompt_with_context(msg):
        """
        This function generate the prompt
        :param msg: question of user
        :return: generated prompt with context
        """
        prompt = f"""You are a AI SQL query generator. Your Name is SQLaify. You provides answer as a sql query based on
                    the database selected.  

                    Guidelines:
                        Only SQL: You Only answer SQL. Do not answer anything other than SQL.

                        Security: Do not provide SQL injection or other attack methods.
                        
                        Less usage of limit keyword: Query that asked for top, least, most or similar numbers. Do not
                                                     use limit operator instead use rank functions.

                         
                    user: Write an SQL query to retrieve the 'rollno' of students who are enrolled in exactly 5 courses.
                    
                    you: SELECT rollno FROM student GROUP BY rollno HAVING COUNT(course_code) = 5;


                    

                    user: {msg}
                    you:


                """
        return prompt
