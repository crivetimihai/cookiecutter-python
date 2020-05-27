"""{{ cookiecutter.package_name }} - {{ cookiecutter.package_description }}"""

__author__ = "{{ cookiecutter.author_name }}"
__copyright__ = "Copyright {{ cookiecutter.year }}, {{ cookiecutter.author_name }}"
__license__ = "{{ cookiecutter.license }}"
__version__ = "{{ cookiecutter.package_version }}"
__date__ = "{% now 'utc', '%Y-%M-%D' %}"
__email__ = "{{ cookiecutter.author_email }}"
__status__ = "Alpha"
__description__ = "{{ cookiecutter.package_description }}"
__url__ = "{{ cookiecutter.github_url }}"
__download_url__ = "{{ cookiecutter.github_url }}"
__packages__ = ["{{ cookiecutter.package_name }}"]

__all__ = ["my_function"]

from .my_module import my_function
