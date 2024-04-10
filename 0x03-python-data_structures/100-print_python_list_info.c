#include <Python.h>

void print_python_list_info(PyObject *p)
{
    int i;
    Py_ssize_t size = PyList_GET_SIZE(p);

    printf("[*] Size of the Python List = %lu\n", size);
    printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < ((PyVarObject *)p)->ob_size; i++)
	{
        printf("Element %d: %s\n", i,
			((PyListObject *)p)->ob_item[i]->ob_type->tp_name);
    }
}