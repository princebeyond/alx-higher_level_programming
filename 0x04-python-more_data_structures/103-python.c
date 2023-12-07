#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python list - prints info
 * @p: A Pyobject
 */
void print_python_list(PyObject *p)
{
	int size, alloc, i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var-> ob_size;
	alloc = list->allocated;

	printf("[*} Python list info\n");
	printf("[*} Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("[*} Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic info about a Python bytes object
 * @p: PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	/**PyBytesObject *bytes = (PyBytesObject *)p;*/
	ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first 10 bytes:");
	for (i = 0; i < size && i < 10; ++i)
	{
		printf(" %02hhx", str[i]);
	}
	printf("\n");
}
