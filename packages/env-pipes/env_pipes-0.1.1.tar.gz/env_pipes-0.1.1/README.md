# env_pipes

Use complex data structures on your environmental variables.

## Actions available

Currently the module insludes some utilitary functions.

### pack_path(*paths_to_pack, base64_result = False, quote_result = False)

This function will accept any number of paths as `paths_to_pack` and create a JSON object with all the content. The files will be encoded as base64 and the directory structure will be preserved.

All the paths provided, regardless of the original location, will end up at the *root* of the package; when unpacked they will all end up on the same target directory, completelly different from the `tar` command. This can be leveraged to pack a *group of files* instead of a directory by doing `paths_to_pack path/to/some/dir/*.*` which will then can be unpacked in any other directory (disregarding tree structure).

The `base64_result` flag will trigger an extra encoding layer, by encoding the resulting object with base64 and returning a *safe* string.

The `quote_result` flag will pass the result through [shlex.quote](https://docs.python.org/dev/library/shlex.html#shlex.quote). That function's behavior will change depending on the shell being used, so plan accordingly.

The quoting feature, if requested, is applied after `base64_result`, so if both flags are supplied the JSON object is encoded and then quoted.

### unpack_path(destination, content_file, create_destination = False, base64_decode = False)

This is the reverse of `pack_path`: it will take a JSON packed `content_file` and dump the decoded files into `destination`.

The `create_destination` flag will create the `destination`, including all the missing parents, if it doesn't exists.

With `base64_decode` you can undo a `paths_to_pack --base64_result` result: the supplied `content_file` is base64 decoded first, then parsed as a JSON file.

### vars_from_file(file_with_vars, sep = ' ')

Load variables from a file (JSON) and outputs a line usable by `env`. You could use a different separator for other use cases: `vars_from_file --sep "\n"`, on a shell/command that understand `\n` as a new line character, would generate a list, useful for scripting, maybe.

## Examples

Creating a JSON object from the files and directories in `path_to_abc_dir/*`
```
$python -m env_pipes pack_path path_to_abc_dir/*
{"a": {"a.txt": "YQo="}, "b.txt": "Ygo=", "c": {"c sub": {"c.txt": "IGMK"}}}
```

Unpack the previous result into `~/Desktop/test`
```
$echo '{"a": {"a.txt": "YQo="}, "b.txt": "Ygo=", "c": {"c sub": {"c.txt": "IGMK"}}}' | python -m env_pipes unpack_path ~/Desktop/test/ -
[PosixPath('/home/user/Desktop/test/a'),
 PosixPath('/home/user/Desktop/test/a/a.txt'),
 PosixPath('/home/user/Desktop/test/b.txt'),
 PosixPath('/home/user/Desktop/test/c'),
 PosixPath('/home/user/Desktop/test/c/c sub'),
 PosixPath('/home/user/Desktop/test/c/c sub/c.txt')]
```

Unpack the same results from a file
```
$python -m env_pipes unpack_path ~/Desktop/test/ packed_abc.json
[PosixPath('/home/user/Desktop/test/a'),
 PosixPath('/home/user/Desktop/test/a/a.txt'),
 PosixPath('/home/user/Desktop/test/b.txt'),
 PosixPath('/home/user/Desktop/test/c'),
 PosixPath('/home/user/Desktop/test/c/c sub'),
 PosixPath('/home/user/Desktop/test/c/c sub/c.txt')]
```
