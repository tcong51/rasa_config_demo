# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import re
import requests
import json
from rasa_sdk.interfaces import ACTION_LISTEN_NAME
from requests.models import encode_multipart_formdata, parse_url
import random
class action_report(Action):

    def name(self) -> Text:
        return "action_report"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #==================================================
        category_report = tracker.get_slot("category_report")
        type_report = tracker.get_slot("type_report")
        unit_report = tracker.get_slot("unit_report")
        day_report = tracker.get_slot("day_report")
        month_report = tracker.get_slot("month_report")
        quarter_report =tracker.get_slot("quarter_report")
        year_report = tracker.get_slot("year_report")
        # day_to_day = tracker.get_slot("mini_day")
        day_m_end = tracker.get_slot("day_m_end")
        # print(day_m_end)
        #==================================================
        def typing_type(category):
            data = {
                    "TKC": [
                    'Viễn thông trả trước',
                    'Viễn thông trả sau',
                    'Viễn thông trả trước và trả sau',
                    'Công nghệ thông tin trả trước',
                    'Công nghệ thông tin trả sau',
                    'Công nghệ thông tin trả trước và trả sau',
                    'Đa dịch vụ trả trước',
                    'Đa dịch vụ trả sau',
                    'Đa dịch vụ trả trước và trả sau'
                    ],
                    "VLR": [
                        'Bật máy',
                        '3G',
                        '4G'
                    ],
                    "DTTT": [
                        'Theo loại dịch vụ trả sau',
                        'Theo loại dịch vụ trả trước',
                        'Theo loại dịch vụ trả trước và trả sau',
                        'Theo chi nhánh trả trước',
                        'Theo chi nhánh trả sau',
                        'Theo chi nhánh trả trước và trả sau'
                    ],
                    "PTTB": [
                        'Trả trước',
                        'Trả sau',
                        'Khách hàng cá nhân',
                        'Khách hàng doanh nghiệp'
                    ],
                    "LUULUONG": [
                        'Data',
                        'Thoại'
                    ],
                    }
            
            offer = data[category]
            num = len(offer)
            stack = 5
            if(num < 5):
                stack = num
                num = num + 1
                arr = random.sample(range(1,num), stack)
                brr = ''
                for i in arr:
                    brr = brr + " --\n"   + offer[i-1]
                dispatcher.utter_message("Vui lòng nhập loại báo cáo! Gợi ý: " + brr)  
            else:
                brr = ''
                arr = random.sample(range(1,num), stack)
                for i in arr:
                    brr = brr + " --\n"   + offer[i-1]  
                dispatcher.utter_message("Vui lòng nhập loại báo cáo! Gợi ý: \n" + brr) 
        #==================================================
        def report_MY(m_y):
            print("M-Y")
        def report_QY(q_y):
            print("Q-Y")
        def report_Y(y):
            print("Y")
        def report_DDMY(d_to_d):
            print("DD-M-Y")
        def report_DMDMY(d_m_e):
            print("DM-DM-Y")
        #==================================================
        # dictrict_unit = {
            # 'Châu Phú'.lower():'AGICPH',
            # 'Châu Thành tỉnh An Giang'.lower():'AGICTH',
            # 'Thị xã Châu Đốc'.lower():'AGICDO',
            # 'Chợ Mới'.lower():'AGICMO',
            # 'Thoại Sơn'.lower():'AGITSO',
            # 'Tri Tôn'.lower():'AGITTO',
            # 'Thị xã Tân Châu'.lower():'AGITCH',
            # 'Tịnh Biên'.lower():'AGITBI',
            # 'Phú Tân'.lower():'AGIPTA',
            # 'An Phú'.lower():'AGIAPH',
            # 'Hòa Bình'.lower():'BLIHBI',
            # 'Giá Rai'.lower():'BLIGRA',
            # 'Vĩnh Lợi'.lower():'BLIVLO',
            # 'Hồng Dân'.lower():'BLIHDA',
            # 'Thị xã Bạc Liêu'.lower():'BLIBLI',
            # 'Đông Hải'.lower():'BLIDHA',
            # 'Phước Long'.lower():'BLIPLO',
            # 'Cái Nước'.lower():'CMACNU',
            # 'Thới Bình'.lower():'CMATBI',
            # 'Năm Căn'.lower():'CMANCA',
            # 'Ngọc Hiển'.lower():'CMANHI',
            # 'Trần Văn Thời'.lower():'CMATVT',
            # 'Đầm Dơi'.lower():'CMADDO',
            # 'Thành phố Cà Mau'.lower():'CMACMA',
            # 'U Minh'.lower():'CMAUMI',
            # 'Phú Tân'.lower():'CMAPTA',
            # 'Châu Thành A'.lower():'HGICTA',
            # 'Long Mỹ'.lower():'HGILMY',
            # 'Thị xã Ngã Bảy'.lower():'HGINBA',
            # 'Phụng Hiệp'.lower():'HGIPHI',
            # 'Thành phố Vị Thanh'.lower():'HGIVTA',
            # 'Vị Thuỷ'.lower():'HGIVTH',
            # 'Châu Thành tỉnh Kiên Giang'.lower():'KGICTH',
            # 'Phú Quốc'.lower():'KGIPQU',
            # 'U Minh Thượng'.lower():'KGIUMT',
            # 'An Biên'.lower():'KGIABI',
            # 'An Minh'.lower():'KGIAMI',
            # 'Giồng Riềng'.lower():'KGIGRI',
            # 'Gò Quao'.lower():'KGIGQU',
            # 'Thị xã Hà Tiên'.lower():'KGIHTI',
            # 'Hòn Đất'.lower():'KGIHDA',
            # 'Kiên Lương'.lower():'KGIKLU',
            # 'Thành phố Rạch Giá'.lower():'KGIRGI',
            # 'Tân Hiệp'.lower():'KGITHI',
            # 'Vĩnh Thuận'.lower():'KGIVTH',
            # 'Kiên Hải'.lower():'KGIKHA',
            # 'Giang Thành'.lower():'KGIGTH',
            # 'Vĩnh Châu'.lower():'STRVCH',
            # 'Mỹ Xuyên'.lower():'STRMXU',
            # 'Kế Sách'.lower():'STRKSA',
            # 'Long Phú'.lower():'STRLPH',
            # 'Ngã Năm'.lower():'STRNNA',
            # 'Thành phố Sóc Trăng'.lower():'STRSTR',
            # 'Châu Thành tỉnh Sóc Trăng'.lower():'STRCTH',
            # 'Thạnh Trị'.lower():'STRTTR',
            # 'Trần Đề'.lower():'STRTDE',
            # 'Mỹ Tú'.lower():'STRMTU',
            # 'Cù Lao Dung'.lower():'STRCLD',
            # 'Bình Thủy'.lower():'CTHBTH',
            # 'Cờ Đỏ'.lower():'CTHCDO',
            # 'Ninh Kiều'.lower():'CTHNKI',
            # 'Phong Điền'.lower():'CTHPDI',
            # 'Vĩnh Thạnh'.lower():'CTHVTH',
            # 'Ô Môn'.lower():'CTHOMO',
            # 'Cái Răng'.lower():'CTHCRA',
            # 'Thốt Nốt'.lower():'CTHTNO',
            # 'Thới Lai'.lower():'CTHTLA',
            # 'Cầu Ngang'.lower():'TVICNG',
            # 'Duyên Hải'.lower():'TVIDHA',
            # 'Trà Cú'.lower():'TVITCU',
            # 'Thành phố Trà Vinh'.lower():'TVITVI',
            # 'Châu Thành tỉnh Trà Vinh'.lower():'',
            # 'Cầu Kè'.lower():'TVICKE',
            # 'Càng Long'.lower():'TVICLO',
            # 'Tiểu Cần'.lower():'TVITCA',
            # 'Thị xã Duyên Hải'.lower():'TVIDHI',
            # 'Mang Thít'.lower():'VLOMTH',
            # 'Bình Minh'.lower():'VLOBMI',
            # 'Tam Bình'.lower():'VLOTBI',
            # 'Thành phố Vĩnh Long'.lower():'VLOVLO',
            # 'Vũng Liêm'.lower():'VLOVLI',
            # 'Long Hồ'.lower():'VLOLHO',
            # 'Trà Ôn'.lower():'VLOTON',
            # 'Bình Tân'.lower():'VLOBTA',
            # 'Thành phố Cao Lãnh'.lower():'DTHCAH',
            # 'Hồng Ngự'.lower():'DTHHNG',
            # 'Lai Vung'.lower():'DTHLVU',
            # 'Lấp Vò'.lower():'DTHLVO',
            # 'Tam Nông'.lower():'DTHTNO',
            # 'Thanh Bình'.lower():'DTHTBI',
            # 'Tân Hồng'.lower():'DTHTHO',
            # 'Cao Lãnh'.lower():'DTHCLA',
            # 'Châu Thành tỉnh Đồng Tháp'.lower():'DTHCTH',
            # 'Thị xã Sa Đéc'.lower():'DTHSDE',
            # 'Tháp Mười'.lower():'DTHTMU',
            # 'Thị xã Hồng Ngự'.lower():'DTHTHN',
            # 'Ba Tri'.lower():'BTRBTI',
            # 'Bình Đại'.lower():'BTRBDA',
            # 'Châu Thành tỉnh Bến Tre'.lower():'',
            # 'Giồng Trôm'.lower():'BTRGTR',
            # 'Thạnh Phú'.lower():'BTRTPH',
            # 'Thành phố Bến Tre'.lower():'BTRBTR',
            # 'Mỏ Cày Bắc'.lower():'BTRMCB',
            # 'Mỏ Cày Nam'.lower():'BTRMCN',
            # 'Chợ Lách'.lower():'BTRCLA',
            # 'Chợ Gạo'.lower():'TGICGA',
            # 'Cai Lậy'.lower():'TGICLA',
            # 'Châu Thành tỉnh Tiền Giang'.lower():'TGICTH',
            # 'Gò Công Đông'.lower():'TGIGCD',
            # 'Gò Công Tây'.lower():'TGIGCT',
            # 'Tân Phước'.lower():'TGITPH',
            # 'Thành phố Mỹ Tho'.lower():'TGIMTH',
            # 'Thị xã Gò Công'.lower():'TGIGCO',
            # 'Tân Phú Đông'.lower():'TGITPD',
            # 'Cái Bè'.lower():'TGICBE',
            # 'Thị xã Cai Lậy'.lower():'TGICLY'
        # }
        
        unit_company = {
            'Phòng khách hàng doanh nghiệp'.lower(): 'KHDN',
            'Công ty 9'.lower():'CONGTY9',
            'Cần Thơ'.lower():'CTH',
            'Phòng Khách hàng cá nhân'.lower():'KHCN',
            'Phòng Dịch vụ Kỹ thuật'.lower():'DVKT',
            'Phòng Tổng hợp'.lower():'PTH',
            'Phòng Chăm sóc khách hàng'.lower():'CSKH',
            'Phòng Kế toán'.lower():'KT',
            'Tổ Thẩm định'.lower():'TTD',
            'Trà Vinh'.lower():'TVI',
            'Tổ Xét thầu'.lower():'TXT',
            'Vĩnh Long'.lower():'VLO',
            'Đồng Tháp'.lower():'DTH',
            'Bến Tre'.lower():'BTR',
            'Tiền Giang'.lower():'TGI',
            'Phú Quốc'.lower():'PQU',
            'An Giang'.lower():'AGI',
            'Bạc Liêu'.lower():'BLI',
            'Cà Mau'.lower():'CMA',
            'Hậu Giang'.lower():'HGI',
            'Kiên Giang'.lower():'KGI',
            'Sóc Trăng'.lower():'STR',
            'Châu Phú'.lower():'AGICPH',
            'Châu Thành tỉnh An Giang'.lower():'AGICTH',
            'Thị xã Châu Đốc'.lower():'AGICDO',
            'Chợ Mới'.lower():'AGICMO',
            'Thoại Sơn'.lower():'AGITSO',
            'Tri Tôn'.lower():'AGITTO',
            'Thị xã Tân Châu'.lower():'AGITCH',
            'Tịnh Biên'.lower():'AGITBI',
            'Phú Tân tỉnh An Giang'.lower():'AGIPTA',
            'An Phú'.lower():'AGIAPH',
            'Hòa Bình'.lower():'BLIHBI',
            'Giá Rai'.lower():'BLIGRA',
            'Vĩnh Lợi'.lower():'BLIVLO',
            'Hồng Dân'.lower():'BLIHDA',
            'Thị xã Bạc Liêu'.lower():'BLIBLI',
            'Đông Hải'.lower():'BLIDHA',
            'Phước Long'.lower():'BLIPLO',
            'Cái Nước'.lower():'CMACNU',
            'Thới Bình'.lower():'CMATBI',
            'Năm Căn'.lower():'CMANCA',
            'Ngọc Hiển'.lower():'CMANHI',
            'Trần Văn Thời'.lower():'CMATVT',
            'Đầm Dơi'.lower():'CMADDO',
            'Thành phố Cà Mau'.lower():'CMACMA',
            'U Minh'.lower():'CMAUMI',
            'Phú Tân tỉnh Cà Mau'.lower():'CMAPTA',
            'Châu Thành A'.lower():'HGICTA',
            'Long Mỹ'.lower():'HGILMY',
            'Thị xã Ngã Bảy'.lower():'HGINBA',
            'Phụng Hiệp'.lower():'HGIPHI',
            'Thành phố Vị Thanh'.lower():'HGIVTA',
            'Vị Thuỷ'.lower():'HGIVTH',
            'Châu Thành tỉnh Kiên Giang'.lower():'KGICTH',
            'Phú Quốc'.lower():'KGIPQU',
            'U Minh Thượng'.lower():'KGIUMT',
            'An Biên'.lower():'KGIABI',
            'An Minh'.lower():'KGIAMI',
            'Giồng Riềng'.lower():'KGIGRI',
            'Gò Quao'.lower():'KGIGQU',
            'Thị xã Hà Tiên'.lower():'KGIHTI',
            'Hòn Đất'.lower():'KGIHDA',
            'Kiên Lương'.lower():'KGIKLU',
            'Thành phố Rạch Giá'.lower():'KGIRGI',
            'Tân Hiệp'.lower():'KGITHI',
            'Vĩnh Thuận'.lower():'KGIVTH',
            'Kiên Hải'.lower():'KGIKHA',
            'Giang Thành'.lower():'KGIGTH',
            'Vĩnh Châu'.lower():'STRVCH',
            'Mỹ Xuyên'.lower():'STRMXU',
            'Kế Sách'.lower():'STRKSA',
            'Long Phú'.lower():'STRLPH',
            'Ngã Năm'.lower():'STRNNA',
            'Thành phố Sóc Trăng'.lower():'STRSTR',
            'Châu Thành tỉnh Sóc Trăng'.lower():'STRCTH',
            'Thạnh Trị'.lower():'STRTTR',
            'Trần Đề'.lower():'STRTDE',
            'Mỹ Tú'.lower():'STRMTU',
            'Cù Lao Dung'.lower():'STRCLD',
            'Bình Thủy'.lower():'CTHBTH',
            'Cờ Đỏ'.lower():'CTHCDO',
            'Ninh Kiều'.lower():'CTHNKI',
            'Phong Điền'.lower():'CTHPDI',
            'Vĩnh Thạnh'.lower():'CTHVTH',
            'Ô Môn'.lower():'CTHOMO',
            'Cái Răng'.lower():'CTHCRA',
            'Thốt Nốt'.lower():'CTHTNO',
            'Thới Lai'.lower():'CTHTLA',
            'Cầu Ngang'.lower():'TVICNG',
            'Duyên Hải'.lower():'TVIDHA',
            'Trà Cú'.lower():'TVITCU',
            'Thành phố Trà Vinh'.lower():'TVITVI',
            'Châu Thành tỉnh Trà Vinh'.lower():'',
            'Cầu Kè'.lower():'TVICKE',
            'Càng Long'.lower():'TVICLO',
            'Tiểu Cần'.lower():'TVITCA',
            'Thị xã Duyên Hải'.lower():'TVIDHI',
            'Mang Thít'.lower():'VLOMTH',
            'Bình Minh'.lower():'VLOBMI',
            'Tam Bình'.lower():'VLOTBI',
            'Thành phố Vĩnh Long'.lower():'VLOVLO',
            'Vũng Liêm'.lower():'VLOVLI',
            'Long Hồ'.lower():'VLOLHO',
            'Trà Ôn'.lower():'VLOTON',
            'Bình Tân'.lower():'VLOBTA',
            'Thành phố Cao Lãnh'.lower():'DTHCAH',
            'Hồng Ngự'.lower():'DTHHNG',
            'Lai Vung'.lower():'DTHLVU',
            'Lấp Vò'.lower():'DTHLVO',
            'Tam Nông'.lower():'DTHTNO',
            'Thanh Bình'.lower():'DTHTBI',
            'Tân Hồng'.lower():'DTHTHO',
            'Cao Lãnh'.lower():'DTHCLA',
            'Châu Thành tỉnh Đồng Tháp'.lower():'DTHCTH',
            'Thị xã Sa Đéc'.lower():'DTHSDE',
            'Tháp Mười'.lower():'DTHTMU',
            'Thị xã Hồng Ngự'.lower():'DTHTHN',
            'Ba Tri'.lower():'BTRBTI',
            'Bình Đại'.lower():'BTRBDA',
            'Châu Thành tỉnh Bến Tre'.lower():'',
            'Giồng Trôm'.lower():'BTRGTR',
            'Thạnh Phú'.lower():'BTRTPH',
            'Thành phố Bến Tre'.lower():'BTRBTR',
            'Mỏ Cày Bắc'.lower():'BTRMCB',
            'Mỏ Cày Nam'.lower():'BTRMCN',
            'Chợ Lách'.lower():'BTRCLA',
            'Chợ Gạo'.lower():'TGICGA',
            'Cai Lậy'.lower():'TGICLA',
            'Châu Thành tỉnh Tiền Giang'.lower():'TGICTH',
            'Gò Công Đông'.lower():'TGIGCD',
            'Gò Công Tây'.lower():'TGIGCT',
            'Tân Phước'.lower():'TGITPH',
            'Thành phố Mỹ Tho'.lower():'TGIMTH',
            'Thị xã Gò Công'.lower():'TGIGCO',
            'Tân Phú Đông'.lower():'TGITPD',
            'Cái Bè'.lower():'TGICBE',
            'Thị xã Cai Lậy'.lower():'TGICLY'
        }
        
        
        # ==================================================
        data_report = {
            'Doanh thu tài khoản chính'.lower():'TKC',
            'Doanh thu tài khoản chính Viễn thông trả trước'.lower():'TKC_VT_TT', 
            'Doanh thu tài khoản chính Viễn thông trả sau'.lower():'TKC_VT_TS', 
            'Doanh thu tài khoản chính Viễn thông trả trước và trả sau'.lower():'TKC_VT_TTTS', 
            'Doanh thu tài khoản chính Công nghệ thông tin trả trước'.lower():'TKC_CNTT_TT', 
            'Doanh thu tài khoản chính Công nghệ thông tin trả sau'.lower():'TKC_CNTT_TS',
            'Doanh thu tài khoản chính Công nghệ thông tin trả trước và trả sau'.lower():'TKC_CNTT_TTTS',
            'Doanh thu tài khoản chính Đa dịch vụ trả trước'.lower():'TKC_DDV_TT',
            'Doanh thu tài khoản chính Đa dịch vụ trả sau'.lower():'TKC_DDV_TS',
            'Doanh thu Tài khoản chính Đa dịch vụ trả trước và trả sau'.lower():'TKC_DDV_TTTS',
            'Kết quả thực hiện các chỉ tiêu kinh doanh'.lower():'KQTHCTKD',
            'Thuê bao VLR'.lower():'VLR',
            'Thuê bao VLR Bật máy'.lower():'VLR_BM',
            'Thuê bao VLR 3G'.lower():'VLR_3G',
            'Thuê bao VLR 4G'.lower():'VLR_4G',
            'Doanh thu thông tin'.lower():'DTTT',
            'Doanh thu thông tin Theo loại dịch vụ trả trước'.lower():'DTTT_DV_TT',
            'Doanh thu thông tin Theo loại dịch vụ trả sau'.lower():'DTTT_DV_TS',
            'Doanh thu thông tin Theo loại dịch vụ trả trước và trả sau'.lower():'DTTT_DV_TTTS',
            'Doanh thu thông tin Theo chi nhánh trả trước'.lower():'DTTT_CN_TT',
            'Doanh thu thông tin Theo chi nhánh trả sau'.lower():'DTTT_CN_TS',
            'Doanh thu thông tin Theo chi nhánh trả trước và trả sau'.lower():'DTTT_CN_TTTS',
            'Doanh thu bán hàng'.lower():'DTBH',
            'Phát triển thuê bao'.lower():'PTTB',
            'Phát triển thuê bao Trả trước'.lower():'PTTB_TT',
            'Phát triển thuê bao Trả sau'.lower():'PTTB_TS',
            'Phát triển thuê bao Khách hàng cá nhân'.lower():'PTTB_KHCN',
            'Phát triển thuê bao Khách hàng doanh nghiệp'.lower():'PTTB_KHDN',
            'Lưu lượng'.lower():'LUULUONG',
            'Lưu lượng Thoại'.lower():'LUULUONG_THOAI',
            'Lưu lượng Data'.lower():'LUULUONG_DATA'
        }
        #==================================================

        KQTHCCTKD = 'kết quả thực hiện các chỉ tiêu kinh doanh'.lower()
        DTBH = 'Doanh thu bán hàng'.lower()
        #==================================================
        reportCode = ''
        provinceCode =''
        districtCode =''
        month = ''
        quarter = ''
        year = ''
        fromDate = ''
        toDate = ''
        
        if(category_report is not None and type_report is not None and unit_report is not None):
            if(day_report is not None and month_report is not None and year_report is not None):
                content = category_report + ' ' + type_report
                content = content.lower()
                pType = data_report[content]
                unit_report_ac = unit_report.lower()
                pName = unit_company[unit_report_ac]
                if (pName == 'CONGTY9' or pName == 'CTH' or pName == 'KHCN' or pName == 'DVKT' or pName == 'PTH' or pName == 'CSKH' or pName == 'KHDN' or pName == 'KT' or pName == 'TTD' or pName == 'TVI' or pName == 'TXT' or pName == 'VLO' or pName == 'DTH' or pName == 'BTR' or pName == 'TGI' or pName == 'PQU' or pName == 'AGI' or pName == 'BLI' or pName == 'CMA' or pName == 'HGI' or pName == 'KGI' or pName == 'STR'):
                    provinceCode = pName
                else:
                    provinceCode = pName[0:3]
                    districtCode = pName 
                # dispatcher.utter_message('{\npType: ' + pType + "\n" + 'Dicstrict:' + provinceCode +'pName: ' + pName + '\n' + 'time: ' + day_report +' '+ month_report + ' ' + year_report + '\n}'  )
            elif(month_report is not None and year_report is not None):
                content = category_report + ' ' + type_report
                content = content.lower()
                pType = data_report[content]
                unit_report_ac = unit_report.lower()
                pName = unit_company[unit_report_ac]
                if (pName == 'CONGTY9' or pName == 'CTH' or pName == 'KHCN' or pName == 'DVKT' or pName == 'PTH' or pName == 'CSKH' or pName == 'KHDN' or pName == 'KT' or pName == 'TTD' or pName == 'TVI' or pName == 'TXT' or pName == 'VLO' or pName == 'DTH' or pName == 'BTR' or pName == 'TGI' or pName == 'PQU' or pName == 'AGI' or pName == 'BLI' or pName == 'CMA' or pName == 'HGI' or pName == 'KGI' or pName == 'STR'):
                    provinceCode = pName
                else:
                    districtCode = pName
                    provinceCode = pName[0:3]
                if(re.search("[0-9][0-9]",month_report)):
                    month_temp = re.search("[0-9][0-9]",month_report)
                else:
                    month_temp = re.search("[0-9]",month_report)
                month = month_temp[0]
                year_temp = re.search("[0-9][0-9][0-9][0-9]",year_report)
                year = year_temp[0]
                jsonData = {
                    "reportCode": pType,
                    "provinceCode" : provinceCode,
                    "districtCode" : districtCode,
                    "month" : month,
                    "quarter" : quarter,
                    "year" : year,
                    "fromDate" : fromDate,
                    "toDate" : toDate
                }
                jsonLogin = {
                    "jsonLog": {
                        "channel": "WEB_1GATE",
                        "imei": "00:50:56:87:02:4d",
                        "key": "",
                        "lang": "vi",
                        "lat": "C9-MINHCQ",
                        "lng": "10.151.120.68",
                        "model": "Postman",
                        "os": "win32",
                        "time": "20200720111100",
                        "version": "1.0.0"
                    },
                    "jsonData": {
                        "username": "qlcpnccty9",
                        "password": "qlcpcty9"
                    },
                    "jsonKey": "LOGIN"
                }
                loginAPI = requests.post(
                    'https://loginportal.mobifone9.vn/auth/v1/login', json=jsonLogin)
                resultLoginAPI = json.loads(loginAPI.content)
                token = resultLoginAPI['data']['token']
                # dispatcher.utter_message(json_message=resultLoginAPI)
                # print(resultLoginAPI)
                jsonReport = {
                    "jsonLog": {
                        "channel": "SERVER 1GATE NEW",
                        "imei": "00:50:56:87:02:4d",
                        "key": "",
                        "lang": "vi",
                        "lat": "C9-MINHCQ",
                        "lng": "10.151.120.80",
                        "model": "Postman",
                        "os": "win32",
                        "time": "202005Mo000000",
                        "version": "1.0.0"
                    },
                    "jsonToken": {
                        "key": token
                    },
                    "jsonData": jsonData
                }
                reportAPI = requests.post('https://apiutil.mobifone9.vn/voicecmd/v1/get-report?a=select',json = jsonReport)
                resultReportAPI = json.loads(reportAPI.content)
                dispatcher.utter_message(json_message=resultReportAPI)
            elif(quarter_report is not None and year_report is not None):
                content = category_report + ' ' + type_report
                content = content.lower()
                pType = data_report[content]
                unit_report_ac = unit_report.lower()
                pName = unit_company[unit_report_ac]
                if (pName == 'CONGTY9' or pName == 'CTH' or pName == 'KHCN' or pName == 'DVKT' or pName == 'PTH' or pName == 'CSKH' or pName == 'KHDN' or pName == 'KT' or pName == 'TTD' or pName == 'TVI' or pName == 'TXT' or pName == 'VLO' or pName == 'DTH' or pName == 'BTR' or pName == 'TGI' or pName == 'PQU' or pName == 'AGI' or pName == 'BLI' or pName == 'CMA' or pName == 'HGI' or pName == 'KGI' or pName == 'STR'):
                    provinceCode = pName
                else:
                    districtCode = pName
                    provinceCode = pName[0:3]
                quarter_temp = re.search("[0-9]",quarter_report)
                quarter = quarter_temp[0]
                year_temp = re.search("[0-9][0-9][0-9][0-9]", year_report)
                year = year_temp[0]
                jsonData = {
                    "reportCode": pType,
                    "provinceCode": provinceCode,
                    "districtCode": districtCode,
                    "month": month,
                    "quarter": quarter,
                    "year": year,
                    "fromDate": fromDate,
                    "toDate": toDate
                }
                jsonLogin = {
                    "jsonLog": {
                        "channel": "WEB_1GATE",
                        "imei": "00:50:56:87:02:4d",
                        "key": "",
                        "lang": "vi",
                        "lat": "C9-MINHCQ",
                        "lng": "10.151.120.68",
                        "model": "Postman",
                        "os": "win32",
                        "time": "20200720111100",
                        "version": "1.0.0"
                    },
                    "jsonData": {
                        "username": "qlcpnccty9",
                        "password": "qlcpcty9"
                    },
                    "jsonKey": "LOGIN"
                }
                loginAPI = requests.post(
                    'https://loginportal.mobifone9.vn/auth/v1/login', json=jsonLogin)
                resultLoginAPI = json.loads(loginAPI.content)
                token = resultLoginAPI['data']['token']
                # dispatcher.utter_message(json_message=resultLoginAPI)
                # print(resultLoginAPI)
                jsonReport = {
                    "jsonLog": {
                        "channel": "SERVER 1GATE NEW",
                        "imei": "00:50:56:87:02:4d",
                        "key": "",
                        "lang": "vi",
                        "lat": "C9-MINHCQ",
                        "lng": "10.151.120.80",
                        "model": "Postman",
                        "os": "win32",
                        "time": "202005Mo000000",
                        "version": "1.0.0"
                    },
                    "jsonToken": {
                        "key": token
                    },
                    "jsonData": jsonData
                }
                reportAPI = requests.post(
                    'https://apiutil.mobifone9.vn/voicecmd/v1/get-report?a=select', json=jsonReport)
                resultReportAPI = json.loads(reportAPI.content)
                dispatcher.utter_message(json_message=resultReportAPI)

            elif(day_m_end is not None and year_report is not None):
                content = category_report + ' ' + type_report
                content = content.lower()
                pType = data_report[content]
                unit_report_ac = unit_report.lower()
                pName = unit_company[unit_report_ac]
                if (pName == 'CONGTY9' or pName == 'CTH' or pName == 'KHCN' or pName == 'DVKT' or pName == 'PTH' or pName == 'CSKH' or pName == 'KHDN' or pName == 'KT' or pName == 'TTD' or pName == 'TVI' or pName == 'TXT' or pName == 'VLO' or pName == 'DTH' or pName == 'BTR' or pName == 'TGI' or pName == 'PQU' or pName == 'AGI' or pName == 'BLI' or pName == 'CMA' or pName == 'HGI' or pName == 'KGI' or pName == 'STR'):
                    provinceCode = pName
                else:
                    districtCode = pName
                    provinceCode = pName[0:3]
                year_temp = re.search("[0-9][0-9][0-9][0-9]", year_report)
                year = year_temp[0]
                if(len(day_m_end)>40): # DD/MM/YY - DD/MM/YY
                    content = re.split("\s", day_m_end, 10) # location: day1-1, month1-3, day2-6, month2-8
                    fromDate = content[1] + '/' + content[3] + '/' + content[5]
                    toDate = content[8] + '/' + content[10] + '/' + year
                    jsonData = {
                        "reportCode": pType,
                        "provinceCode": provinceCode,
                        "districtCode": districtCode,
                        "month": month,
                        "quarter": quarter,
                        "year": '',
                        "fromDate": fromDate,
                        "toDate": toDate
                    }
                    # print(jsonData)
                    jsonLogin = {
                        "jsonLog": {
                            "channel": "WEB_1GATE",
                            "imei": "00:50:56:87:02:4d",
                            "key": "",
                            "lang": "vi",
                            "lat": "C9-MINHCQ",
                            "lng": "10.151.120.68",
                            "model": "Postman",
                            "os": "win32",
                            "time": "20200720111100",
                            "version": "1.0.0"
                        },
                        "jsonData": {
                            "username": "qlcpnccty9",
                            "password": "qlcpcty9"
                        },
                        "jsonKey": "LOGIN"
                    }
                    loginAPI = requests.post(
                        'https://loginportal.mobifone9.vn/auth/v1/login', json=jsonLogin)
                    resultLoginAPI = json.loads(loginAPI.content)
                    token = resultLoginAPI['data']['token']
                    # dispatcher.utter_message(json_message=resultLoginAPI)
                    # print(resultLoginAPI)
                    jsonReport = {
                        "jsonLog": {
                            "channel": "SERVER 1GATE NEW",
                            "imei": "00:50:56:87:02:4d",
                            "key": "",
                            "lang": "vi",
                            "lat": "C9-MINHCQ",
                            "lng": "10.151.120.80",
                            "model": "Postman",
                            "os": "win32",
                            "time": "202005Mo000000",
                            "version": "1.0.0"
                        },
                        "jsonToken": {
                            "key": token
                        },
                        "jsonData": jsonData
                    }
                    reportAPI = requests.post(
                        'https://apiutil.mobifone9.vn/voicecmd/v1/get-report?a=select', json=jsonReport)
                    resultReportAPI = json.loads(reportAPI.content)
                    dispatcher.utter_message(json_message=resultReportAPI)
                    # dispatcher.utter_message('{\npType: ' + pType +  '\nprovince:' + provinceCode + 'Dicstrict:' +
                    #                          districtCode + "\n" + '\nformDate: ' + content[1] + '/' + content[3] + '/' + content[5] + ' \ntoDate: ' + content[8] + '/' + content[10] +'/' + year + '\n}')
                elif(30<len(day_m_end)<40): # DD/MM - DD/MM
                    content = re.split("\s", day_m_end, 10) # location: day1-1, month1-3, day2-6, month2-8
                    fromDate = content[1] + '/' + content[3] + '/' + year
                    toDate = content[6] + '/' + content[8] + '/' + year
                    jsonData = {
                        "reportCode": pType,
                        "provinceCode": provinceCode,
                        "districtCode": districtCode,
                        "month": month,
                        "quarter": quarter,
                        "year": '',
                        "fromDate": fromDate,
                        "toDate": toDate
                    }
                    # print(jsonData)
                    jsonLogin = {
                        "jsonLog": {
                            "channel": "WEB_1GATE",
                            "imei": "00:50:56:87:02:4d",
                            "key": "",
                            "lang": "vi",
                            "lat": "C9-MINHCQ",
                            "lng": "10.151.120.68",
                            "model": "Postman",
                            "os": "win32",
                            "time": "20200720111100",
                            "version": "1.0.0"
                        },
                        "jsonData": {
                            "username": "qlcpnccty9",
                            "password": "qlcpcty9"
                        },
                        "jsonKey": "LOGIN"
                    }
                    loginAPI = requests.post(
                        'https://loginportal.mobifone9.vn/auth/v1/login', json=jsonLogin)
                    resultLoginAPI = json.loads(loginAPI.content)
                    token = resultLoginAPI['data']['token']
                    # dispatcher.utter_message(json_message=resultLoginAPI)
                    # print(resultLoginAPI)
                    jsonReport = {
                        "jsonLog": {
                            "channel": "SERVER 1GATE NEW",
                            "imei": "00:50:56:87:02:4d",
                            "key": "",
                            "lang": "vi",
                            "lat": "C9-MINHCQ",
                            "lng": "10.151.120.80",
                            "model": "Postman",
                            "os": "win32",
                            "time": "202005Mo000000",
                            "version": "1.0.0"
                        },
                        "jsonToken": {
                            "key": token
                        },
                        "jsonData": jsonData
                    }
                    reportAPI = requests.post(
                        'https://apiutil.mobifone9.vn/voicecmd/v1/get-report?a=select', json=jsonReport)
                    resultReportAPI = json.loads(reportAPI.content)
                    dispatcher.utter_message(json_message=resultReportAPI)
                    # dispatcher.utter_message('{\npType: ' + pType +  '\nprovince:' + provinceCode + 'Dicstrict:' +
                    #                          districtCode + "\n" + '\nfromDate: ' + content[1] + '/' + content[3] + '/' + year + '\ntoDate: ' + content[6] + '/' + content[8] + '/' + year + '\n}')
                elif( 26<= len(day_m_end)<= 28): # DM - DM/Y
                    content = re.split("\s", day_m_end, 10)
                    fromDate = content[1] + '/' + content[6]+'/'+ year
                    toDate = content[4] + '/' + content[6] +'/'+ year
                    jsonData = {
                        "reportCode": pType,
                        "provinceCode": provinceCode,
                        "districtCode": districtCode,
                        "month": month,
                        "quarter": quarter,
                        "year": '',
                        "fromDate": fromDate,
                        "toDate": toDate
                    }
                    # print(jsonData)
                    jsonLogin = {
                        "jsonLog": {
                            "channel": "WEB_1GATE",
                            "imei": "00:50:56:87:02:4d",
                            "key": "",
                            "lang": "vi",
                            "lat": "C9-MINHCQ",
                            "lng": "10.151.120.68",
                            "model": "Postman",
                            "os": "win32",
                            "time": "20200720111100",
                            "version": "1.0.0"
                        },
                        "jsonData": {
                            "username": "qlcpnccty9",
                            "password": "qlcpcty9"
                        },
                        "jsonKey": "LOGIN"
                    }
                    loginAPI = requests.post(
                        'https://loginportal.mobifone9.vn/auth/v1/login', json=jsonLogin)
                    resultLoginAPI = json.loads(loginAPI.content)
                    token = resultLoginAPI['data']['token']
                    # dispatcher.utter_message(json_message=resultLoginAPI)
                    # print(resultLoginAPI)
                    jsonReport = {
                        "jsonLog": {
                            "channel": "SERVER 1GATE NEW",
                            "imei": "00:50:56:87:02:4d",
                            "key": "",
                            "lang": "vi",
                            "lat": "C9-MINHCQ",
                            "lng": "10.151.120.80",
                            "model": "Postman",
                            "os": "win32",
                            "time": "202005Mo000000",
                            "version": "1.0.0"
                        },
                        "jsonToken": {
                            "key": token
                        },
                        "jsonData": jsonData
                    }
                    reportAPI = requests.post('https://apiutil.mobifone9.vn/voicecmd/v1/get-report?a=select',json = jsonReport)
                    resultReportAPI = json.loads(reportAPI.content)
                    dispatcher.utter_message(json_message=resultReportAPI)
                    # dispatcher.utter_message('{\npType: ' + pType + 'province:' + provinceCode + 'Dicstrict:' +
                                            #  districtCode + "\n" + 'fromDate: ' + content[1] + '/' + content[6]+'/'+year + ' \ntoDate: ' + content[4] + '/' + content[6] + year + '\n}')
                elif(len(day_m_end)==29): # 12/2020 - 1/2021
                    content = re.split("\s", day_m_end, 10)
                    fromDate = content[1] + '/' + content[3]
                    toDate = content[6] + '/' + year
                    jsonData = {
                        "reportCode": pType,
                        "provinceCode": provinceCode,
                        "districtCode": districtCode,
                        "month": month,
                        "quarter": quarter,
                        "year": '',
                        "fromDate": fromDate,
                        "toDate": toDate
                    }
                    # print(jsonData)
                    jsonLogin = {
                        "jsonLog": {
                            "channel": "WEB_1GATE",
                            "imei": "00:50:56:87:02:4d",
                            "key": "",
                            "lang": "vi",
                            "lat": "C9-MINHCQ",
                            "lng": "10.151.120.68",
                            "model": "Postman",
                            "os": "win32",
                            "time": "20200720111100",
                            "version": "1.0.0"
                        },
                        "jsonData": {
                            "username": "qlcpnccty9",
                            "password": "qlcpcty9"
                        },
                        "jsonKey": "LOGIN"
                    }
                    loginAPI = requests.post(
                        'https://loginportal.mobifone9.vn/auth/v1/login', json=jsonLogin)
                    resultLoginAPI = json.loads(loginAPI.content)
                    token = resultLoginAPI['data']['token']
                    # dispatcher.utter_message(json_message=resultLoginAPI)
                    # print(resultLoginAPI)
                    jsonReport = {
                        "jsonLog": {
                            "channel": "SERVER 1GATE NEW",
                            "imei": "00:50:56:87:02:4d",
                            "key": "",
                            "lang": "vi",
                            "lat": "C9-MINHCQ",
                            "lng": "10.151.120.80",
                            "model": "Postman",
                            "os": "win32",
                            "time": "202005Mo000000",
                            "version": "1.0.0"
                        },
                        "jsonToken": {
                            "key": token
                        },
                        "jsonData": jsonData
                    }
                    reportAPI = requests.post(
                        'https://apiutil.mobifone9.vn/voicecmd/v1/get-report?a=select', json=jsonReport)
                    resultReportAPI = json.loads(reportAPI.content)
                    dispatcher.utter_message(json_message=resultReportAPI)
                    # dispatcher.utter_message('{\npType: ' + pType +  'province:' + provinceCode + 'Dicstrict:' +
                    #                      districtCode + "\n"  + 'fromDate: '+ content[1] + '/'+ content[3]+ ' \ntoDate: ' +  content[6] + '/' + year + '\n}'  )
                elif(19<= len(day_m_end)<=21): #MM - MM 
                    content = re.split("\s", day_m_end, 10)
                    fromDate = content[1] + '/' + year
                    toDate = content[4] + '/' + year
                    jsonData = {
                        "reportCode": pType,
                        "provinceCode": provinceCode,
                        "districtCode": districtCode,
                        "month": month,
                        "quarter": quarter,
                        "year": '',
                        "fromDate": fromDate,
                        "toDate": toDate
                    }
                    # print(jsonData)
                    jsonLogin = {
                        "jsonLog": {
                            "channel": "WEB_1GATE",
                            "imei": "00:50:56:87:02:4d",
                            "key": "",
                            "lang": "vi",
                            "lat": "C9-MINHCQ",
                            "lng": "10.151.120.68",
                            "model": "Postman",
                            "os": "win32",
                            "time": "20200720111100",
                            "version": "1.0.0"
                        },
                        "jsonData": {
                            "username": "qlcpnccty9",
                            "password": "qlcpcty9"
                        },
                        "jsonKey": "LOGIN"
                    }
                    loginAPI = requests.post(
                        'https://loginportal.mobifone9.vn/auth/v1/login', json=jsonLogin)
                    resultLoginAPI = json.loads(loginAPI.content)
                    token = resultLoginAPI['data']['token']
                    # dispatcher.utter_message(json_message=resultLoginAPI)
                    # print(resultLoginAPI)
                    jsonReport = {
                        "jsonLog": {
                            "channel": "SERVER 1GATE NEW",
                            "imei": "00:50:56:87:02:4d",
                            "key": "",
                            "lang": "vi",
                            "lat": "C9-MINHCQ",
                            "lng": "10.151.120.80",
                            "model": "Postman",
                            "os": "win32",
                            "time": "202005Mo000000",
                            "version": "1.0.0"
                        },
                        "jsonToken": {
                            "key": token
                        },
                        "jsonData": jsonData
                    }
                    reportAPI = requests.post(
                        'https://apiutil.mobifone9.vn/voicecmd/v1/get-report?a=select', json=jsonReport)
                    resultReportAPI = json.loads(reportAPI.content)
                    dispatcher.utter_message(json_message=resultReportAPI)
                    # dispatcher.utter_message('{\npType: ' + pType + '\nprovince:' + provinceCode + 'Dicstrict:' +
                    #                          districtCode + "\n" + 'fromDate: ' + content[1] + '/' + year + '\n toDate: ' + content[4] + '/' + year + '\n}')
               

            elif(year_report is not None):
                content = category_report + ' ' + type_report
                content = content.lower()
                pType = data_report[content]
                unit_report_ac = unit_report.lower()
                pName = unit_company[unit_report_ac]
                if (pName == 'CONGTY9' or pName == 'CTH' or pName == 'KHCN' or pName == 'DVKT' or pName == 'PTH' or pName == 'CSKH' or pName == 'KHDN' or pName == 'KT' or pName == 'TTD' or pName == 'TVI' or pName == 'TXT' or pName == 'VLO' or pName == 'DTH' or pName == 'BTR' or pName == 'TGI' or pName == 'PQU' or pName == 'AGI' or pName == 'BLI' or pName == 'CMA' or pName == 'HGI' or pName == 'KGI' or pName == 'STR'):
                    provinceCode = pName
                else:
                    districtCode = pName
                    provinceCode = pName[0:3]
                year_temp = re.search("[0-9][0-9][0-9][0-9]", year_report)
                year = year_temp[0]
                jsonData = {
                    "reportCode": pType,
                    "provinceCode": provinceCode,
                    "districtCode": districtCode,
                    "month": month,
                    "quarter": quarter,
                    "year": year,
                    "fromDate": fromDate,
                    "toDate": toDate
                }
                # print(jsonData)
                jsonLogin = {
                    "jsonLog": {
                        "channel": "WEB_1GATE",
                        "imei": "00:50:56:87:02:4d",
                        "key": "",
                        "lang": "vi",
                        "lat": "C9-MINHCQ",
                        "lng": "10.151.120.68",
                        "model": "Postman",
                        "os": "win32",
                        "time": "20200720111100",
                        "version": "1.0.0"
                    },
                    "jsonData": {
                        "username": "qlcpnccty9",
                        "password": "qlcpcty9"
                    },
                    "jsonKey": "LOGIN"
                }
                loginAPI = requests.post(
                    'https://loginportal.mobifone9.vn/auth/v1/login', json=jsonLogin)
                resultLoginAPI = json.loads(loginAPI.content)
                token = resultLoginAPI['data']['token']
                # dispatcher.utter_message(json_message=resultLoginAPI)
                # print(resultLoginAPI)
                jsonReport = {
                    "jsonLog": {
                        "channel": "SERVER 1GATE NEW",
                        "imei": "00:50:56:87:02:4d",
                        "key": "",
                        "lang": "vi",
                        "lat": "C9-MINHCQ",
                        "lng": "10.151.120.80",
                        "model": "Postman",
                        "os": "win32",
                        "time": "202005Mo000000",
                        "version": "1.0.0"
                    },
                    "jsonToken": {
                        "key": token
                    },
                    "jsonData": jsonData
                }
                reportAPI = requests.post(
                    'https://apiutil.mobifone9.vn/voicecmd/v1/get-report?a=select', json=jsonReport)
                resultReportAPI = json.loads(reportAPI.content)
                dispatcher.utter_message(json_message=resultReportAPI)
                # dispatcher.utter_message('{\npType: ' + pType + '\nprovince:' + provinceCode + '\nDicstrict:' +
                #                          districtCode + "\n" + 'time: ' + year + '\n}')
            else:
                dispatcher.utter_message(response="utter_time")     
        elif(category_report is not None and type_report is None and unit_report is not None):
            category_report = category_report.lower()
            if(category_report == KQTHCCTKD or category_report == DTBH):
                if(day_report is not None and month_report is not None and year_report is not None):
                    content = category_report.lower()
                    pType = data_report[content]
                    unit_report_ac = unit_report.lower()
                    pName = unit_company[unit_report_ac]
                    if (pName == 'CONGTY9' or pName == 'CTH' or pName == 'KHCN' or pName == 'DVKT' or pName == 'PTH' or pName == 'CSKH' or pName == 'KHDN' or pName == 'KT' or pName == 'TTD' or pName == 'TVI' or pName == 'TXT' or pName == 'VLO' or pName == 'DTH' or pName == 'BTR' or pName == 'TGI' or pName == 'PQU' or pName == 'AGI' or pName == 'BLI' or pName == 'CMA' or pName == 'HGI' or pName == 'KGI' or pName == 'STR'):
                        provinceCode = pName
                    else:
                        districtCode = pName
                        provinceCode = pName[0:3]
                    # dispatcher.utter_message('{\npType: ' + pType + 'province:' + provinceCode + 'Dicstrict:' +
                    #                          districtCode + "\n" "\n" + 'pName: ' + pName + '\n' + 'time: ' + day_report + ' ' + month_report + ' ' + year_report + '\n}')
                elif(month_report is not None and year_report is not None):
                    content = category_report.lower()
                    pType = data_report[content]
                    unit_report_ac = unit_report.lower()
                    pName = unit_company[unit_report_ac]
                    if (pName == 'CONGTY9' or pName == 'CTH' or pName == 'KHCN' or pName == 'DVKT' or pName == 'PTH' or pName == 'CSKH' or pName == 'KHDN' or pName == 'KT' or pName == 'TTD' or pName == 'TVI' or pName == 'TXT' or pName == 'VLO' or pName == 'DTH' or pName == 'BTR' or pName == 'TGI' or pName == 'PQU' or pName == 'AGI' or pName == 'BLI' or pName == 'CMA' or pName == 'HGI' or pName == 'KGI' or pName == 'STR'):
                        provinceCode = pName
                    else:
                        districtCode = pName
                        provinceCode = pName[0:3]
                    if(re.search("[0-9][0-9]", month_report)):
                        month_temp = re.search("[0-9][0-9]", month_report)
                    else:
                        month_temp = re.search("[0-9]", month_report)
                    month = month_temp[0]
                    year_temp = re.search("[0-9][0-9][0-9][0-9]", year_report)
                    year = year_temp[0]
                    jsonData = {
                        "reportCode": pType,
                        "provinceCode": provinceCode,
                        "districtCode": districtCode,
                        "month": month,
                        "quarter": quarter,
                        "year": year,
                        "fromDate": fromDate,
                        "toDate": toDate
                    }
                    jsonLogin = {
                        "jsonLog": {
                            "channel": "WEB_1GATE",
                            "imei": "00:50:56:87:02:4d",
                            "key": "",
                            "lang": "vi",
                            "lat": "C9-MINHCQ",
                            "lng": "10.151.120.68",
                            "model": "Postman",
                            "os": "win32",
                            "time": "20200720111100",
                            "version": "1.0.0"
                        },
                        "jsonData": {
                            "username": "qlcpnccty9",
                            "password": "qlcpcty9"
                        },
                        "jsonKey": "LOGIN"
                    }
                    loginAPI = requests.post(
                        'https://loginportal.mobifone9.vn/auth/v1/login', json=jsonLogin)
                    resultLoginAPI = json.loads(loginAPI.content)
                    token = resultLoginAPI['data']['token']

                    jsonReport = {
                        "jsonLog": {
                            "channel": "SERVER 1GATE NEW",
                            "imei": "00:50:56:87:02:4d",
                            "key": "",
                            "lang": "vi",
                            "lat": "C9-MINHCQ",
                            "lng": "10.151.120.80",
                            "model": "Postman",
                            "os": "win32",
                            "time": "202005Mo000000",
                            "version": "1.0.0"
                        },
                        "jsonToken": {
                            "key": token
                        },
                        "jsonData": jsonData
                    }
                    reportAPI = requests.post(
                        'https://apiutil.mobifone9.vn/voicecmd/v1/get-report?a=select', json=jsonReport)
                    resultReportAPI = json.loads(reportAPI.content)
                    dispatcher.utter_message(json_message=resultReportAPI)

                elif(quarter_report is not None and year_report is not None):
                    content = category_report.lower()
                    pType = data_report[content]
                    unit_report_ac = unit_report.lower()
                    pName = unit_company[unit_report_ac]
                    if (pName == 'CONGTY9' or pName == 'CTH' or pName == 'KHCN' or pName == 'DVKT' or pName == 'PTH' or pName == 'CSKH' or pName == 'KHDN' or pName == 'KT' or pName == 'TTD' or pName == 'TVI' or pName == 'TXT' or pName == 'VLO' or pName == 'DTH' or pName == 'BTR' or pName == 'TGI' or pName == 'PQU' or pName == 'AGI' or pName == 'BLI' or pName == 'CMA' or pName == 'HGI' or pName == 'KGI' or pName == 'STR'):
                        provinceCode = pName
                    else:
                        districtCode = pName
                        provinceCode = pName[0:3]
                    quarter_temp = re.search("[0-9]", quarter_report)
                    quarter = quarter_temp[0]
                    year_temp = re.search("[0-9][0-9][0-9][0-9]", year_report)
                    year = year_temp[0]
                    jsonData = {
                    "reportCode": pType,
                    "provinceCode": provinceCode,
                    "districtCode": districtCode,
                    "month": month,
                    "quarter": quarter,
                    "year": year,
                    "fromDate": fromDate,
                    "toDate": toDate
                    }
                    jsonLogin = {
                        "jsonLog": {
                            "channel": "WEB_1GATE",
                            "imei": "00:50:56:87:02:4d",
                            "key": "",
                            "lang": "vi",
                            "lat": "C9-MINHCQ",
                            "lng": "10.151.120.68",
                            "model": "Postman",
                            "os": "win32",
                            "time": "20200720111100",
                            "version": "1.0.0"
                        },
                        "jsonData": {
                            "username": "qlcpnccty9",
                            "password": "qlcpcty9"
                        },
                        "jsonKey": "LOGIN"
                    }
                    loginAPI = requests.post(
                        'https://loginportal.mobifone9.vn/auth/v1/login', json=jsonLogin)
                    resultLoginAPI = json.loads(loginAPI.content)
                    token = resultLoginAPI['data']['token']
                    # dispatcher.utter_message(json_message=resultLoginAPI)
                    # print(resultLoginAPI)
                    jsonReport = {
                        "jsonLog": {
                            "channel": "SERVER 1GATE NEW",
                            "imei": "00:50:56:87:02:4d",
                            "key": "",
                            "lang": "vi",
                            "lat": "C9-MINHCQ",
                            "lng": "10.151.120.80",
                            "model": "Postman",
                            "os": "win32",
                            "time": "202005Mo000000",
                            "version": "1.0.0"
                        },
                        "jsonToken": {
                            "key": token
                        },
                        "jsonData": jsonData
                    }
                    reportAPI = requests.post(
                        'https://apiutil.mobifone9.vn/voicecmd/v1/get-report?a=select', json=jsonReport)
                    resultReportAPI = json.loads(reportAPI.content)
                    dispatcher.utter_message(json_message=resultReportAPI)
                        

                elif(day_m_end is not None and year_report is not None):
                    content = category_report.lower()
                    pType = data_report[content]
                    unit_report_ac = unit_report.lower()
                    pName = unit_company[unit_report_ac]
                    if (pName == 'CONGTY9' or pName == 'CTH' or pName == 'KHCN' or pName == 'DVKT' or pName == 'PTH' or pName == 'CSKH' or pName == 'KHDN' or pName == 'KT' or pName == 'TTD' or pName == 'TVI' or pName == 'TXT' or pName == 'VLO' or pName == 'DTH' or pName == 'BTR' or pName == 'TGI' or pName == 'PQU' or pName == 'AGI' or pName == 'BLI' or pName == 'CMA' or pName == 'HGI' or pName == 'KGI' or pName == 'STR'):
                        provinceCode = pName
                    else:
                        districtCode = pName
                        provinceCode = pName[0:3]
                    year_temp = re.search("[0-9][0-9][0-9][0-9]", year_report)
                    year = year_temp[0]
                    if(len(day_m_end) > 40):  # DD/MM/YY - DD/MM/YY
                        # location: day1-1, month1-3, day2-6, month2-8
                        content = re.split("\s", day_m_end, 10)
                        fromDate = content[1] + '/' + content[3] + '/' + content[5]
                        toDate = content[8] + '/' + content[10] + '/' + year
                        jsonData = {
                            "reportCode": pType,
                            "provinceCode": provinceCode,
                            "districtCode": districtCode,
                            "month": month,
                            "quarter": quarter,
                            "year": '',
                            "fromDate": fromDate,
                            "toDate": toDate
                        }
                        # print(jsonData)
                        jsonLogin = {
                            "jsonLog": {
                                "channel": "WEB_1GATE",
                                "imei": "00:50:56:87:02:4d",
                                "key": "",
                                "lang": "vi",
                                "lat": "C9-MINHCQ",
                                "lng": "10.151.120.68",
                                "model": "Postman",
                                "os": "win32",
                                "time": "20200720111100",
                                "version": "1.0.0"
                            },
                            "jsonData": {
                                "username": "qlcpnccty9",
                                "password": "qlcpcty9"
                            },
                            "jsonKey": "LOGIN"
                        }
                        loginAPI = requests.post(
                            'https://loginportal.mobifone9.vn/auth/v1/login', json=jsonLogin)
                        resultLoginAPI = json.loads(loginAPI.content)
                        token = resultLoginAPI['data']['token']
                        # dispatcher.utter_message(json_message=resultLoginAPI)
                        # print(resultLoginAPI)
                        jsonReport = {
                            "jsonLog": {
                                "channel": "SERVER 1GATE NEW",
                                "imei": "00:50:56:87:02:4d",
                                "key": "",
                                "lang": "vi",
                                "lat": "C9-MINHCQ",
                                "lng": "10.151.120.80",
                                "model": "Postman",
                                "os": "win32",
                                "time": "202005Mo000000",
                                "version": "1.0.0"
                            },
                            "jsonToken": {
                                "key": token
                            },
                            "jsonData": jsonData
                        }
                        reportAPI = requests.post(
                            'https://apiutil.mobifone9.vn/voicecmd/v1/get-report?a=select', json=jsonReport)
                        resultReportAPI = json.loads(reportAPI.content)
                        dispatcher.utter_message(json_message=resultReportAPI)
                        # dispatcher.utter_message('{\npType: ' + pType +  '\nprovince:' + provinceCode + 'Dicstrict:' +
                        #                          districtCode + "\n" + '\nformDate: ' + content[1] + '/' + content[3] + '/' + content[5] + ' \ntoDate: ' + content[8] + '/' + content[10] +'/' + year + '\n}')
                    elif(30 < len(day_m_end) < 40):  # DD/MM - DD/MM
                        # location: day1-1, month1-3, day2-6, month2-8
                        content = re.split("\s", day_m_end, 10)
                        fromDate = content[1] + '/' + content[3] + '/' + year
                        toDate = content[6] + '/' + content[8] + '/' + year
                        jsonData = {
                            "reportCode": pType,
                            "provinceCode": provinceCode,
                            "districtCode": districtCode,
                            "month": month,
                            "quarter": quarter,
                            "year": '',
                            "fromDate": fromDate,
                            "toDate": toDate
                        }
                        # print(jsonData)
                        jsonLogin = {
                            "jsonLog": {
                                "channel": "WEB_1GATE",
                                "imei": "00:50:56:87:02:4d",
                                "key": "",
                                "lang": "vi",
                                "lat": "C9-MINHCQ",
                                "lng": "10.151.120.68",
                                "model": "Postman",
                                "os": "win32",
                                "time": "20200720111100",
                                "version": "1.0.0"
                            },
                            "jsonData": {
                                "username": "qlcpnccty9",
                                "password": "qlcpcty9"
                            },
                            "jsonKey": "LOGIN"
                        }
                        loginAPI = requests.post(
                            'https://loginportal.mobifone9.vn/auth/v1/login', json=jsonLogin)
                        resultLoginAPI = json.loads(loginAPI.content)
                        token = resultLoginAPI['data']['token']
                        # dispatcher.utter_message(json_message=resultLoginAPI)
                        # print(resultLoginAPI)
                        jsonReport = {
                            "jsonLog": {
                                "channel": "SERVER 1GATE NEW",
                                "imei": "00:50:56:87:02:4d",
                                "key": "",
                                "lang": "vi",
                                "lat": "C9-MINHCQ",
                                "lng": "10.151.120.80",
                                "model": "Postman",
                                "os": "win32",
                                "time": "202005Mo000000",
                                "version": "1.0.0"
                            },
                            "jsonToken": {
                                "key": token
                            },
                            "jsonData": jsonData
                        }
                        reportAPI = requests.post(
                            'https://apiutil.mobifone9.vn/voicecmd/v1/get-report?a=select', json=jsonReport)
                        resultReportAPI = json.loads(reportAPI.content)
                        dispatcher.utter_message(json_message=resultReportAPI)
                        # dispatcher.utter_message('{\npType: ' + pType +  '\nprovince:' + provinceCode + 'Dicstrict:' +
                        #                          districtCode + "\n" + '\nfromDate: ' + content[1] + '/' + content[3] + '/' + year + '\ntoDate: ' + content[6] + '/' + content[8] + '/' + year + '\n}')
                    elif(26 <= len(day_m_end) <= 28):  # DM - DM/Y
                        content = re.split("\s", day_m_end, 10)
                        fromDate = content[1] + '/' + content[6]+'/' + year
                        toDate = content[4] + '/' + content[6] + '/'+ year
                        jsonData = {
                            "reportCode": pType,
                            "provinceCode": provinceCode,
                            "districtCode": districtCode,
                            "month": month,
                            "quarter": quarter,
                            "year": '',
                            "fromDate": fromDate,
                            "toDate": toDate
                        }
                        # print(jsonData)
                        jsonLogin = {
                            "jsonLog": {
                                "channel": "WEB_1GATE",
                                "imei": "00:50:56:87:02:4d",
                                "key": "",
                                "lang": "vi",
                                "lat": "C9-MINHCQ",
                                "lng": "10.151.120.68",
                                "model": "Postman",
                                "os": "win32",
                                "time": "20200720111100",
                                "version": "1.0.0"
                            },
                            "jsonData": {
                                "username": "qlcpnccty9",
                                "password": "qlcpcty9"
                            },
                            "jsonKey": "LOGIN"
                        }
                        loginAPI = requests.post(
                            'https://loginportal.mobifone9.vn/auth/v1/login', json=jsonLogin)
                        resultLoginAPI = json.loads(loginAPI.content)
                        token = resultLoginAPI['data']['token']
                        # dispatcher.utter_message(json_message=resultLoginAPI)
                        # print(resultLoginAPI)
                        jsonReport = {
                            "jsonLog": {
                                "channel": "SERVER 1GATE NEW",
                                "imei": "00:50:56:87:02:4d",
                                "key": "",
                                "lang": "vi",
                                "lat": "C9-MINHCQ",
                                "lng": "10.151.120.80",
                                "model": "Postman",
                                "os": "win32",
                                "time": "202005Mo000000",
                                "version": "1.0.0"
                            },
                            "jsonToken": {
                                "key": token
                            },
                            "jsonData": jsonData
                        }
                        reportAPI = requests.post(
                            'https://apiutil.mobifone9.vn/voicecmd/v1/get-report?a=select', json=jsonReport)
                        resultReportAPI = json.loads(reportAPI.content)
                        dispatcher.utter_message(json_message=resultReportAPI)
                        # dispatcher.utter_message('{\npType: ' + pType + 'province:' + provinceCode + 'Dicstrict:' +
                        #  districtCode + "\n" + 'fromDate: ' + content[1] + '/' + content[6]+'/'+year + ' \ntoDate: ' + content[4] + '/' + content[6] + year + '\n}')
                    elif(len(day_m_end) == 29):  # 12/2020 - 1/2021
                        content = re.split("\s", day_m_end, 10)
                        fromDate = content[1] + '/' + content[3]
                        toDate = content[6] + '/' + year
                        jsonData = {
                            "reportCode": pType,
                            "provinceCode": provinceCode,
                            "districtCode": districtCode,
                            "month": month,
                            "quarter": quarter,
                            "year": '',
                            "fromDate": fromDate,
                            "toDate": toDate
                        }
                        # print(jsonData)
                        jsonLogin = {
                            "jsonLog": {
                                "channel": "WEB_1GATE",
                                "imei": "00:50:56:87:02:4d",
                                "key": "",
                                "lang": "vi",
                                "lat": "C9-MINHCQ",
                                "lng": "10.151.120.68",
                                "model": "Postman",
                                "os": "win32",
                                "time": "20200720111100",
                                "version": "1.0.0"
                            },
                            "jsonData": {
                                "username": "qlcpnccty9",
                                "password": "qlcpcty9"
                            },
                            "jsonKey": "LOGIN"
                        }
                        loginAPI = requests.post(
                            'https://loginportal.mobifone9.vn/auth/v1/login', json=jsonLogin)
                        resultLoginAPI = json.loads(loginAPI.content)
                        token = resultLoginAPI['data']['token']
                        # dispatcher.utter_message(json_message=resultLoginAPI)
                        # print(resultLoginAPI)
                        jsonReport = {
                            "jsonLog": {
                                "channel": "SERVER 1GATE NEW",
                                "imei": "00:50:56:87:02:4d",
                                "key": "",
                                "lang": "vi",
                                "lat": "C9-MINHCQ",
                                "lng": "10.151.120.80",
                                "model": "Postman",
                                "os": "win32",
                                "time": "202005Mo000000",
                                "version": "1.0.0"
                            },
                            "jsonToken": {
                                "key": token
                            },
                            "jsonData": jsonData
                        }
                        reportAPI = requests.post('https://apiutil.mobifone9.vn/voicecmd/v1/get-report?a=select',json = jsonReport)
                        resultReportAPI = json.loads(reportAPI.content)
                        dispatcher.utter_message(json_message=resultReportAPI)
                        # dispatcher.utter_message('{\npType: ' + pType +  'province:' + provinceCode + 'Dicstrict:' +
                        #                      districtCode + "\n"  + 'fromDate: '+ content[1] + '/'+ content[3]+ ' \ntoDate: ' +  content[6] + '/' + year + '\n}'  )
                    elif(19 <= len(day_m_end) <= 21):  # MM - MM
                        content = re.split("\s", day_m_end, 10)
                        fromDate = content[1] + '/' + year
                        toDate = content[4] + '/' + year
                        jsonData = {
                            "reportCode": pType,
                            "provinceCode": provinceCode,
                            "districtCode": districtCode,
                            "month": month,
                            "quarter": quarter,
                            "year": '',
                            "fromDate": fromDate,
                            "toDate": toDate
                        }
                        # print(jsonData)
                        jsonLogin = {
                            "jsonLog": {
                                "channel": "WEB_1GATE",
                                "imei": "00:50:56:87:02:4d",
                                "key": "",
                                "lang": "vi",
                                "lat": "C9-MINHCQ",
                                "lng": "10.151.120.68",
                                "model": "Postman",
                                "os": "win32",
                                "time": "20200720111100",
                                "version": "1.0.0"
                            },
                            "jsonData": {
                                "username": "qlcpnccty9",
                                "password": "qlcpcty9"
                            },
                            "jsonKey": "LOGIN"
                        }
                        loginAPI = requests.post(
                            'https://loginportal.mobifone9.vn/auth/v1/login', json=jsonLogin)
                        resultLoginAPI = json.loads(loginAPI.content)
                        token = resultLoginAPI['data']['token']
                        # dispatcher.utter_message(json_message=resultLoginAPI)
                        # print(resultLoginAPI)
                        jsonReport = {
                            "jsonLog": {
                                "channel": "SERVER 1GATE NEW",
                                "imei": "00:50:56:87:02:4d",
                                "key": "",
                                "lang": "vi",
                                "lat": "C9-MINHCQ",
                                "lng": "10.151.120.80",
                                "model": "Postman",
                                "os": "win32",
                                "time": "202005Mo000000",
                                "version": "1.0.0"
                            },
                            "jsonToken": {
                                "key": token
                            },
                            "jsonData": jsonData
                        }
                        reportAPI = requests.post('https://apiutil.mobifone9.vn/voicecmd/v1/get-report?a=select',json = jsonReport)
                        resultReportAPI = json.loads(reportAPI.content)
                        dispatcher.utter_message(json_message=resultReportAPI)
                elif(year_report is not None):
                    content = category_report.lower()
                    pType = data_report[content]
                    unit_report_ac = unit_report.lower()
                    pName = unit_company[unit_report_ac]
                    if (pName == 'CONGTY9' or pName == 'CTH' or pName == 'KHCN' or pName == 'DVKT' or pName == 'PTH' or pName == 'CSKH' or pName == 'KHDN' or pName == 'KT' or pName == 'TTD' or pName == 'TVI' or pName == 'TXT' or pName == 'VLO' or pName == 'DTH' or pName == 'BTR' or pName == 'TGI' or pName == 'PQU' or pName == 'AGI' or pName == 'BLI' or pName == 'CMA' or pName == 'HGI' or pName == 'KGI' or pName == 'STR'):
                        provinceCode = pName
                    else:
                        districtCode = pName
                        provinceCode = pName[0:3]
                    year_temp = re.search("[0-9][0-9][0-9][0-9]", year_report)
                    year = year_temp[0]
                    jsonData = {
                    "reportCode": pType,
                    "provinceCode": provinceCode,
                    "districtCode": districtCode,
                    "month": month,
                    "quarter": quarter,
                    "year": year,
                    "fromDate": fromDate,
                    "toDate": toDate
                    }
                    # print(jsonData)
                    jsonLogin = {
                        "jsonLog": {
                            "channel": "WEB_1GATE",
                            "imei": "00:50:56:87:02:4d",
                            "key": "",
                            "lang": "vi",
                            "lat": "C9-MINHCQ",
                            "lng": "10.151.120.68",
                            "model": "Postman",
                            "os": "win32",
                            "time": "20200720111100",
                            "version": "1.0.0"
                        },
                        "jsonData": {
                            "username": "qlcpnccty9",
                            "password": "qlcpcty9"
                        },
                        "jsonKey": "LOGIN"
                    }
                    loginAPI = requests.post(
                        'https://loginportal.mobifone9.vn/auth/v1/login', json=jsonLogin)
                    resultLoginAPI = json.loads(loginAPI.content)
                    token = resultLoginAPI['data']['token']
                    # dispatcher.utter_message(json_message=resultLoginAPI)
                    # print(resultLoginAPI)
                    jsonReport = {
                        "jsonLog": {
                            "channel": "SERVER 1GATE NEW",
                            "imei": "00:50:56:87:02:4d",
                            "key": "",
                            "lang": "vi",
                            "lat": "C9-MINHCQ",
                            "lng": "10.151.120.80",
                            "model": "Postman",
                            "os": "win32",
                            "time": "202005Mo000000",
                            "version": "1.0.0"
                        },
                        "jsonToken": {
                            "key": token
                        },
                        "jsonData": jsonData
                    }
                    reportAPI = requests.post(
                        'https://apiutil.mobifone9.vn/voicecmd/v1/get-report?a=select', json=jsonReport)
                    resultReportAPI = json.loads(reportAPI.content)
                    dispatcher.utter_message(json_message=resultReportAPI)
                    # dispatcher.utter_message('{\npType: ' + pType + '\nprovince:' + provinceCode + '\nDicstrict:' +
                    #                      districtCode + "\n" + 'time: ' + year + '\n}')  # ========================================= #
                else:
                    dispatcher.utter_message(response="utter_time")
            elif(category_report is not KQTHCCTKD or category_report is not DTBH):
                # dispatcher.utter_message("Nhập type")
                content = category_report.lower()
                pType = data_report[content]
                typing_type(pType)
                # dispatcher.utter_message(response="utter_typing_type")
        elif(category_report is not None and type_report is not None and unit_report is None):
            # dispatcher.utter_message("nhap uNit đi chứ") 
            dispatcher.utter_message(response="utter_typing_unit")
        elif(category_report is not None and type_report is None and unit_report is None):
            if(category_report == KQTHCCTKD or category_report == DTBH):
                # dispatcher.utter_message("nhap unit 2")
                dispatcher.utter_message(response="utter_typing_unit")
            elif(category_report is not KQTHCCTKD or category_report is not DTBH):
                # dispatcher.utter_message("nhap type")
                content = category_report.lower()
                pType = data_report[content]
                typing_type(pType)
                # dispatcher.utter_message(response="utter_typing_type")
        elif(category_report is None and unit_report is not None):
            # dispatcher.utter_message("nhập category đi chứ")
            dispatcher.utter_message(response="utter_typing_category")
        #==================================================
        return []
