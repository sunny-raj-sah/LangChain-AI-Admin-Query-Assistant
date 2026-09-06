# # from langchain_openai import ChatOpenAI
# from langchain_groq import ChatGroq
# from langchain.agents.agent_types import AgentType
# from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
# import os
# from dotenv import load_dotenv

# load_dotenv()

# class QueryEngine:
#     def __init__(self, dataframe, temperature=0):
#         """
#         Initialize LangChain agent with pandas DataFrame
#         """
#         self.df = dataframe
#         # self.llm = ChatOpenAI(
#         #     temperature=temperature,
#         #     model="gpt-3.5-turbo",
#         #     openai_api_key=os.getenv("OPENAI_API_KEY")
#         # )
#         self.llm = ChatGroq(
#           temperature=temperature,
#           model=os.getenv("GROQ_MODEL"),
#           groq_api_key=os.getenv("GROQ_API_KEY")
#         )
        
#         # self.agent = create_pandas_dataframe_agent(
#         #     self.llm,
#         #     self.df,
#         #     verbose=True,
#         #     agent_type=AgentType.OPENAI_FUNCTIONS,
#         #     allow_dangerous_code=True  # Required for pandas operations
#         # )
#         # self.agent = create_pandas_dataframe_agent(
#         #     llm=self.llm,
#         #     df=self.df,
#         #     agent_type=AgentType.TOOL_CALLING,
#         #     verbose=True,
#         #     allow_dangerous_code=True,
#         # )
#         self.agent = create_pandas_dataframe_agent(
#              llm=self.llm,
#              df=self.df,
#              agent_type=AgentType.TOOL_CALLING,
#              verbose=True,
#              allow_dangerous_code=True,
#          )
    
#     def query(self, question):
#         """
#         Process natural language query and return results
#         """
#         try:
#             # Add context to help the agent understand the data
#             context = f"""
#             You are analyzing student data with the following columns:
#             {', '.join(self.df.columns.tolist())}
            
#             Current date context: November 2025
            
#             User question: {question}
            
#             Provide a clear, concise answer. If returning data, format it nicely.
#             """
            
#             response = self.agent.invoke(context)
#             return response['output']
        
#         except Exception as e:
#             return f"Error processing query: {str(e)}"
    
#     def get_dataframe_info(self):
#         """Return basic info about the accessible data"""
#         return {
#             "total_records": len(self.df),
#             "columns": self.df.columns.tolist(),
#             "sample": self.df.head(3).to_dict('records')
#         }


# -----------------------------------------------------------------------------

from langchain_groq import ChatGroq
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import os
from dotenv import load_dotenv

load_dotenv()

class QueryEngine:
    def __init__(self, dataframe, temperature=0):
        """
        Initialize LangChain agent with pandas DataFrame
        """
        self.df = dataframe

        self.llm = ChatGroq(
            temperature=temperature,
            model=os.getenv("GROQ_MODEL"),
            groq_api_key=os.getenv("GROQ_API_KEY")
        )

        self.agent = create_pandas_dataframe_agent(
            llm=self.llm,
            df=self.df,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            allow_dangerous_code=True,
        )

    def query(self, question):
        """
        Process natural language query and return results
        """
        try:
            context = f"""
            You are analyzing student data with the following columns:
            {', '.join(self.df.columns.tolist())}

            Current date context: November 2025

            User question: {question}

            Provide a clear, concise answer. If returning data, format it nicely.
            """

            response = self.agent.invoke(context)
            return response['output']

        except Exception as e:
            return f"Error processing query: {str(e)}"

    def get_dataframe_info(self):
        """Return basic info about the accessible data"""
        return {
            "total_records": len(self.df),
            "columns": self.df.columns.tolist(),
            "sample": self.df.head(3).to_dict('records')
        }
