#!/usr/bin/env python
# coding: utf-8

# In[285]:


input_value = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}
 


# In[288]:


def test(d):
    import json
    for k in d.keys():
        d2 = d[k]
        for k2 in d2.keys():
            d3 = d2[k2]
            for k3 in d3.keys():
                d4 = d3[k3]
                for k4 in d4.keys():
                    k4 = k4
                    for v in d4.values():
                        v = v
    output_value={}
    output_value[v]= {}
    output_value[v][k4]= {}
    output_value[v][k4][k3]= {}
    output_value[v][k4][k3][k2]= {}
    output_value[v][k4][k3][k2]= k
    print("output_value =" ,  json.dumps(output_value,sort_keys=True, indent=4))


# In[289]:


test(input_value)

