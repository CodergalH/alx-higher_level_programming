#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_bytes(PyObject *p)
{
    char str = p;
    printf("[.] bytes object info\n");
    printf("  size: %lu\n", ((PyVarObject *)p)->ob_size);
    printf("  trying string: %s", str);

    Py_ssize_t len = strlen(p);

    if(len > 0 && len <= 9)
    {
        printf("  first %lu bytes: ", len + 1);
        for (int i=0; i < len + 1; i++)
            printf("%02hhx ", p[i]);
    }
    else if(len >= 10)
    {
        printf("  first %d bytes: ", 10);
        for (int i=0; i < 10; i++)
            printf("%02hhx ", p[i]);
    }
    printf("\n");

    return (0);
}

void print_python_bytes(PyObject *p)
{
    int i;
    Py_ssize_t size = PyList_GET_SIZE(p);

    printf("[*] Python list info");
    printf("[*] size of the Python list = %lu\n", size);
    printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < ((PyVarObject *)p)->ob_size; i++)
		printf("Element %d: ", i);

    int type = Py_IS_TYPE(((PyListObject *)p)->ob_item[i], 'bytes');
    
    if (type == 1)
        print_python_bytes(((PyListObject *)p)->ob_item[i]);
    else
        printf("%s\n", ((PyTypeObject *)p)->tp_name);

    printf("\n");

}