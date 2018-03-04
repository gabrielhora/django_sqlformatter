import logging
import sqlparse
from pygments import highlight
from pygments.lexers.sql import SqlLexer
from pygments.formatters.terminal import TerminalFormatter


class SqlFormatter(logging.Formatter):
    """
    Format and syntax highlight SQL queries for the terminal
    """

    def format(self, record):
        try:
            sql = sqlparse.format(
                record.sql,
                keyword_case='upper',
                identifier_case='lower',
                truncate_strings=50,
                reindent=True).strip('\n')
            sql = '\n\t| '.join([l for l in sql.split('\n')])
            sql = highlight(sql, SqlLexer(), TerminalFormatter())
            return '({:.3f}) | {}'.format(record.duration, sql)
        except:
            # fall back to the default formatting if anything happens
            return super().format(record)
