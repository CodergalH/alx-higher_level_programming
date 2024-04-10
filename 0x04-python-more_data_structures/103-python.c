#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_bytes - prints info about python lists
 * @p: address of pyobject struct
 */
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

void print_python_bytes(PyObject *p)
{
    size_t i, len;
    char *str;

    printf("[.] bytes object info\n");
    if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
    printf("  size: %lu\n", ((PyVarObject *)p)->ob_size);
    str = ((PyBytesObject *)p)->ob_sval;
    printf("  trying string: %s\n", str);

    len = strlen(str);

    if(len > 0 && len <= 9)
    {
        printf("  first %lu bytes: ", len + 1);
        for (i = 0; i < len + 1; i++)
            printf(" %02hhx", str[i]);
    }
    else if(len >= 10)
    {
        printf("  first %d bytes: ", 10);
        for (int i=0; i < 10; i++)
            printf(" %02hhx", str[i]);
    }
    printf("\n");
}


/**
 * print_python_list - prints info about python lists
 * @p: address of pyobject struct
 */
void print_python_list(PyObject *p)
{
    int i;
    Py_ssize_t size = PyList_GET_SIZE(p);

    printf("[*] Python list info");
    printf("[*] size of the Python list = %lu\n", size);
    printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < ((PyVarObject *)p)->ob_size; i++)
	{
        printf("Element %d: %s\n", i,
			((PyListObject *)p)->ob_item[i]->ob_type->tp_name);
		if (!strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
    }

    printf("\n");
}