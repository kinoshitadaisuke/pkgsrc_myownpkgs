# $NetBSD$

DISTNAME=	instagrapi-2.1.3
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	python net
MASTER_SITES=	${MASTER_SITE_PYPI:=i/instagrapi/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/subzeroid/instagrapi
COMMENT=	Fast and effective Instagram Private API wrapper
LICENSE=	mit

# net
DEPENDS+=	${PYPKGPREFIX}-Socks>=1.7.1:../../net/py-Socks

# devel
DEPENDS+=	${PYPKGPREFIX}-pydantic>=2.10.1:../../devel/py-pydantic
DEPENDS+=	${PYPKGPREFIX}-requests>=2.25.1:../../devel/py-requests

# pkgsrc_myownpkgs
DEPENDS+=	${PYPKGPREFIX}-pycryptodomex>=3.21.0:../../pkgsrc_myownpkgs/py-pycryptodomex

USE_LANGUAGES=	# none

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
