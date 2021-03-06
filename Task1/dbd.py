SQL_DBD_Init = """\
pragma foreign_keys = on;

begin transaction;


create table dbd$domains (
    id  integer primary key autoincrement default(null),
    name varchar unique default(null),
    description varchar default(null),
    data_type_id integer not null,
    length integer default(null),
    char_length integer default(null),
    precision integer default(null),
    scale integer default(null),
    width integer default(null),
    align char default(null),
    show_null boolean default(null),
    show_lead_nulls boolean default(null),
    thousands_separator boolean default(null),
    summable boolean default(null),
    case_sensitive boolean default(null),
    abstract_domain boolean default(null)
);

create index "idx.FZX832TFV" on dbd$domains(data_type_id);



create table dbd$schemas (
    id integer primary key autoincrement not null,
    name varchar not null
);




create table dbd$tables (
    id integer primary key autoincrement default(null),
    schema_id integer default(null),
    name varchar unique,
    description varchar default(null),
    can_add boolean default(null),
    can_edit boolean default(null),
    can_delete boolean default(null),
    temporal_mode varchar default(null),
    access_level integer default(null),
    ht_table_flags varchar default(null),
    means varchar default(null)
);

create table dbd$table_custom (
    id integer primary key autoincrement default(null),
    table_id integer,
    ddl_text blob
);


create table dbd$fields (
    id integer primary key autoincrement default(null),
    table_id integer not null,
    position integer not null,
    name varchar not null,
    russian_short_name varchar not null,
    description varchar default(null),
    domain_id integer not null,
    can_input boolean default(null),
    can_edit boolean default(null),
    show_in_grid boolean default(null),
    show_in_details boolean default(null),
    is_mean boolean default(null),
    autocalculated boolean default(null),
    required boolean default(null)
);

create index "idx.7UAKR6FT7" on dbd$fields(table_id);
create index "idx.7HJ6KZXJF" on dbd$fields(position);
create index "idx.74RSETF9N" on dbd$fields(name);
create index "idx.6S0E8MWZV" on dbd$fields(domain_id);


create table dbd$settings (
    key varchar primary key not null,
    value varchar,
    valueb BLOB
);


create table dbd$constraints (
    id integer primary key autoincrement default (null),
    table_id integer not null,
    name varchar default(null),
    constraint_type char default(null),
    reference integer default(null),
    unique_key_id integer default(null),
    has_value_edit boolean default(null),
    cascading_delete boolean default(null),
    expression varchar default(null)
);

create index "idx.6F902GEQ3" on dbd$constraints(table_id);
create index "idx.6SRYJ35AJ" on dbd$constraints(name);
create index "idx.62HLW9WGB" on dbd$constraints(constraint_type);
create index "idx.5PQ7Q3E6J" on dbd$constraints(reference);
create index "idx.92GH38TZ4" on dbd$constraints(unique_key_id);



create table dbd$constraint_details (
    id integer primary key autoincrement default(null),
    constraint_id integer not null,
    position integer not null,
    field_id integer not null default(null)
);

create index "idx.5CYTJWVWR" on dbd$constraint_details(constraint_id);
create index "idx.507FDQDMZ" on dbd$constraint_details(position);
create index "idx.4NG17JVD7" on dbd$constraint_details(field_id);





create table dbd$indices (
    id integer primary key autoincrement default(null),
    table_id integer not null,
    name varchar default(null),
    local boolean default(0),
    kind char default(null)
);

create index "idx.12XXTJUYZ" on dbd$indices(table_id);
create index "idx.6G0KCWN0R" on dbd$indices(name);


create table dbd$index_details (
    id integer primary key autoincrement default(null),
    index_id integer not null,
    position integer not null,
    field_id integer default(null),
    expression varchar default(null),
    descend boolean default(null)
);

create index "idx.H1KFOWTCB" on dbd$index_details(index_id);
create index "idx.BQA4HXWNF" on dbd$index_details(field_id);


create table dbd$data_types (
    id integer primary key autoincrement,
    type_id varchar unique
);

insert into dbd$data_types(type_id) values ('STRING');
insert into dbd$data_types(type_id) values ('SMALLINT');
insert into dbd$data_types(type_id) values ('INTEGER');
insert into dbd$data_types(type_id) values ('WORD');
insert into dbd$data_types(type_id) values ('BOOLEAN');
insert into dbd$data_types(type_id) values ('FLOAT');
insert into dbd$data_types(type_id) values ('CURRENCY');
insert into dbd$data_types(type_id) values ('BCD');
insert into dbd$data_types(type_id) values ('FMTBCD');
insert into dbd$data_types(type_id) values ('DATE');
insert into dbd$data_types(type_id) values ('TIME');
insert into dbd$data_types(type_id) values ('DATETIME');
insert into dbd$data_types(type_id) values ('TIMESTAMP');
insert into dbd$data_types(type_id) values ('BYTES');
insert into dbd$data_types(type_id) values ('VARBYTES');
insert into dbd$data_types(type_id) values ('BLOB');
insert into dbd$data_types(type_id) values ('MEMO');
insert into dbd$data_types(type_id) values ('GRAPHIC');
insert into dbd$data_types(type_id) values ('FMTMEMO');
insert into dbd$data_types(type_id) values ('FIXEDCHAR');
insert into dbd$data_types(type_id) values ('WIDESTRING');
insert into dbd$data_types(type_id) values ('LARGEINT');
insert into dbd$data_types(type_id) values ('COMP');
insert into dbd$data_types(type_id) values ('ARRAY');
insert into dbd$data_types(type_id) values ('FIXEDWIDECHAR');
insert into dbd$data_types(type_id) values ('WIDEMEMO');
insert into dbd$data_types(type_id) values ('CODE');
insert into dbd$data_types(type_id) values ('RECORDID');
insert into dbd$data_types(type_id) values ('SET');
insert into dbd$data_types(type_id) values ('PERIOD');
insert into dbd$data_types(type_id) values ('BYTE');
insert into dbd$settings(key, value) values ('dbd.version', '%(dbd_version)s');

create view dbd$view_fields as
select
  dbd$schemas.name "schema",
  dbd$tables.name "table",
  dbd$fields.position "position",
  dbd$fields.name "name",
  dbd$fields.russian_short_name "russian_short_name",
  dbd$fields.description "description",
  dbd$data_types.type_id "type_id",
  dbd$domains.length "length",
  dbd$domains.char_length,
  dbd$domains.width "width",
  dbd$domains.align "align",
  dbd$domains.precision "precision",
  dbd$domains.scale "scale",
  dbd$domains.show_null "show_null",
  dbd$domains.show_lead_nulls "show_lead_nulls",
  dbd$domains.thousands_separator "thousands_separator",
  dbd$domains.summable,
  dbd$domains.case_sensitive "case_sensitive",
  dbd$domains.abstract_domain,
  dbd$fields.can_input "can_input",
  dbd$fields.can_edit "can_edit",
  dbd$fields.show_in_grid "show_in_grid",
  dbd$fields.show_in_details "show_in_details",
  dbd$fields.is_mean "is_mean",
  dbd$fields.autocalculated "autocalculated",
  dbd$fields.required "required"
from dbd$fields
  inner join dbd$tables on dbd$fields.table_id = dbd$tables.id
  inner join dbd$domains on dbd$fields.domain_id = dbd$domains.id
  inner join dbd$data_types on dbd$domains.data_type_id = dbd$data_types.id
  Left Join dbd$schemas On dbd$tables.schema_id = dbd$schemas.id
order by
  dbd$tables.name,
  dbd$fields.position;

create view dbd$view_domains as
select
  dbd$domains.id,
  dbd$domains.name,
  dbd$domains.description,
  dbd$data_types.type_id,
  dbd$domains.length,
  dbd$domains.char_length,
  dbd$domains.width,
  dbd$domains.align,
  dbd$domains.summable,
  dbd$domains.precision,
  dbd$domains.scale,
  dbd$domains.show_null,
  dbd$domains.show_lead_nulls,
  dbd$domains.thousands_separator,
  dbd$domains.case_sensitive "case_sensitive",
  dbd$domains.abstract_domain
from dbd$domains
  inner join dbd$data_types on dbd$domains.data_type_id = dbd$data_types.id
order by dbd$domains.id;

create view dbd$view_constraints as
select
  dbd$constraints.id "constraint_id",
  dbd$constraints.constraint_type "constraint_type",
  dbd$constraint_details.position "position",
  dbd$schemas.name "schema",
  dbd$tables.name "table_name",
  dbd$fields.name "field_name",
  "references".name "reference"
from
  dbd$constraint_details
  inner join dbd$constraints on dbd$constraint_details.constraint_id = dbd$constraints.id
  inner join dbd$tables on dbd$constraints.table_id = dbd$tables.id
  left join dbd$tables "references" on dbd$constraints.reference = "references".id
  left join dbd$fields on dbd$constraint_details.field_id = dbd$fields.id
  Left Join dbd$schemas On dbd$tables.schema_id = dbd$schemas.id
order by
  constraint_id, position;

create view dbd$view_indices as
select
  dbd$indices.id "index_id",
  dbd$indices.name as index_name,
  dbd$schemas.name "schema",
  dbd$tables.name as table_name,
  dbd$indices.local,
  dbd$indices.kind,
  dbd$index_details.position,
  dbd$fields.name as field_name,
  dbd$index_details.expression,
  dbd$index_details.descend
from
  dbd$index_details
  inner join dbd$indices on dbd$index_details.index_id = dbd$indices.id
  inner join dbd$tables on dbd$indices.table_id = dbd$tables.id
  left join dbd$fields on dbd$index_details.field_id = dbd$fields.id
  Left Join dbd$schemas On dbd$tables.schema_id = dbd$schemas.id
order by
  dbd$tables.name, dbd$indices.name, dbd$index_details.position;

commit;
""" % {'dbd_version': 2.1}