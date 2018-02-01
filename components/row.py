import uuid;
class Row(dict):
    _id=0;
    _uid=0;
    global _data;
    _data = dict();
    def __init__(self, value, **kwargs):
        super(Row, self).__init__(**kwargs)
        self.update(value)
        Row._uid = uuid.uuid4();
        Row._id = id(self);

    def id(self):
        return Row._id;

    def uid(self):
        return Row._uid;

    def update(self, value, **kwargs):
        _data.update(value,**kwargs);





