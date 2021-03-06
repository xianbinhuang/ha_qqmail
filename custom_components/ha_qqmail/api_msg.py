from homeassistant.helpers import template

class ApiMsg():

    def __init__(self, hass, mail):
        self.hass = hass
        self.mail = mail

    # 模板解析
    def template(self, _message):
        self.mail.log('【模板解析前】：' + _message)
        # 解析模板
        tpl = template.Template(_message, self.hass)
        _message = tpl.async_render(None)
        self.mail.log('【模板解析后】：' + _message)
        return _message

    # 默认消息
    def default(self, title, entity, action, base_url):
        
        # 只有消息
        if entity is None and action is None:            
            return self.template(msg)

        _entity = ''
        if entity is not None:
            for item in entity.split(','):
                _entity += "'" + item.strip() + "',"

        _action = ''
        if action is not None:
            for item in action.split(','):
                _action += "'" + item.strip() + "',"

        # 生成md5文件

        # 传入md5

        msg = '''
        <div style="box-shadow: 0 1px 2px #aaa;">
            <div style="padding:20px 20px 0 20px;font-weight:bold;font-size:20px;">
                ''' + title + '''
            </div>
            <div style="padding:20px;border-bottom:1px solid #ddd;">        
                {% set arr = [''' + _entity.strip(',') + '''] %}
                {% for id in arr -%}
                <div style="display: flex; justify-content: space-between; border-top:1px solid #eee;padding:10px 20px;">
                    <span>{{states[id].attributes.friendly_name}}</span>
                    <span>{{ states(id) }}</span>
                </div>
                {%- endfor %}
            </div>
            <div style="text-align: right;padding:0 10px 10px 10px;">
            {% set arr = [''' + _action.strip(',') + '''] %}
            {% for id in arr -%}
            <a href="''' + base_url + '''?action={{id}}" style="display:inline-block;padding:10px 20px;margin-left:10px;margin-top:10px;background:#03a9f4;color:white;text-decoration: none;font-size:14px;">
            {{states[id].attributes.friendly_name}}
            </a>
            {%- endfor %}
            </div>
        </div>
        '''
        return self.template(msg)