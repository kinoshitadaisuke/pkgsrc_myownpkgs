# $NetBSD$

DISTNAME=	aiobotocore-3.1.3
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=a/aiobotocore/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/aio-libs/aiobotocore
COMMENT=	Async client for aws services using botocore and aiohttp
LICENSE=	apache-2.0

DEPENDS+=	${PYPKGPREFIX}-botocore>=1.29.76:../../net/py-botocore
DEPENDS+=	${PYPKGPREFIX}-aiohttp>=3.3.1:../../www/py-aiohttp
DEPENDS+=	${PYPKGPREFIX}-wrapt>=1.10.10:../../devel/py-wrapt
DEPENDS+=	# TODO: aioitertools>=0.5.1

USE_LANGUAGES=	# none

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
