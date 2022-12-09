/** @odoo-module **/

import { registerPatch, patchModelMethods } from '@mail/model/model_core';
import { attr } from '@mail/model/model_field';
// ensure that the model definition is loaded before the patch
// import '@mail/models/message';

registerPatch({
    name : 'Message',
    fields:{
        cc_partners: attr(),
        bcc_partners: attr(),
        email_cc: attr(),
        email_bcc: attr(),
    },
    modelMethods :{

    /**
     * @override
    */
    convertData(data) {
        const data2 = this._super(data);
        if ('cc_partners' in data && data.cc_partners) {
            if (!data2.cc_partners) {
                data2.cc_partners = data.cc_partners;
            }                
        }
        if ('bcc_partners' in data && data.bcc_partners) {
            if (!data2.bcc_partners) {
                data2.bcc_partners = data.bcc_partners;
            }
        }
        if ('email_cc' in data && data.email_cc) {
            if (!data2.email_cc) {
                data2.email_cc = data.email_cc
            }
        }
        if ('email_bcc' in data && data.email_bcc) {
            if (!data2.email_bcc) {
                data2.email_bcc = data.email_bcc
            }
        }
        return data2;
    },
}

});

/* Copyright (c) 2015-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>) */
/* See LICENSE file for full copyright and licensing details. */
/* License URL : <https://store.webkul.com/license.html/> */