/*
 * Copyright (c) 2020 YuQing <384681@qq.com>
 *
 * This program is free software: you can use, redistribute, and/or modify
 * it under the terms of the GNU Affero General Public License, version 3
 * or later ("AGPL"), as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program. If not, see <https://www.gnu.org/licenses/>.
 */


#ifndef _SERVER_TYPES_H
#define _SERVER_TYPES_H

#include "sf/sf_types.h"
#include "fastdir/client/fdir_client.h"
#include "common/auth_types.h"

#define AUTH_FIXED_USER_COUNT  256

#define TASK_STATUS_CONTINUE           12345
#define TASK_ARG          ((AuthServerTaskArg *)task->arg)
#define TASK_CTX          TASK_ARG->context
#define REQUEST           TASK_CTX.common.request
#define RESPONSE          TASK_CTX.common.response
#define RESPONSE_STATUS   RESPONSE.header.status
#define REQUEST_STATUS    REQUEST.header.status
#define SERVER_TASK_TYPE  TASK_CTX.task_type

#define SERVER_CTX        ((AuthServerContext *)task->thread_data->arg)

typedef struct auth_user_info {
    string_t username;
    int64_t priv;
} AuthUserInfo;

typedef struct auth_user_array {
    AuthUserInfo *users;
    AuthUserInfo fixed[AUTH_FIXED_USER_COUNT];
    int count;
    int alloc;
} AuthUserArray;

typedef struct server_task_arg {
    struct {
        SFCommonTaskContext common;
        int task_type;
    } context;
} AuthServerTaskArg;

typedef struct auth_server_context {
    FDIRClientContext client_ctx;
} AuthServerContext;

#endif