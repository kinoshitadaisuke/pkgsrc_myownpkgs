# $NetBSD$

DISTNAME=	s3fs-2024.3.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	sysutils python
MASTER_SITES=	${MASTER_SITE_PYPI:=s/s3fs/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/s3fs/
COMMENT=	Convenient Filesystem interface over S3
LICENSE=	modified-bsd

PYTHON_VERSIONS_INCOMPATIBLE=	27 37

DEPENDS+=	${PYPKGPREFIX}-aiobotocore>=2.5.0:../../pkgsrc_myownpkgs/py-aiobotocore
DEPENDS+=	${PYPKGPREFIX}-fsspec>=2023.4.0:../../sysutils/py-fsspec
DEPENDS+=	${PYPKGPREFIX}-aiohttp>=0:../../www/py-aiohttp
DEPENDS+=	${PYPKGPREFIX}-awscli>=0:../../net/py-awscli
DEPENDS+=	${PYPKGPREFIX}-boto3>=0:../../net/py-boto3
DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools

# url2pkg-marker (please do not remove this line.)
.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
