# $NetBSD$

DISTNAME=	mercantile-1.2.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	pkgsrc_myownpkgs python
MASTER_SITES=	${MASTER_SITE_PYPI:=m/mercantile/}

MAINTAINER=	INSERT_YOUR_MAIL_ADDRESS_HERE # or use pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/mapbox/mercantile
COMMENT=	Web mercator XYZ tile utilities
#LICENSE=	BSD # TODO: from setup.py; needs to be adjusted

TOOL_DEPENDS+=	${PYPKGPREFIX}-check-manifest>=0:../../wip/py-check-manifest
DEPENDS+=	${PYPKGPREFIX}-click>=3.0:../../devel/py-click

DEPENDS+=	${PYPKGPREFIX}-attrs>=0:../../devel/py-attrs
DEPENDS+=	${PYPKGPREFIX}-certifi>=0:../../security/py-certifi
DEPENDS+=	${PYPKGPREFIX}-chardet>=0:../../converters/py-chardet
DEPENDS+=	${PYPKGPREFIX}-coverage>=0:../../devel/py-coverage
DEPENDS+=	${PYPKGPREFIX}-coveralls>=0:../../devel/py-coveralls
DEPENDS+=	${PYPKGPREFIX}-docopt>=0:../../devel/py-docopt
DEPENDS+=	${PYPKGPREFIX}-hypothesis>=0:../../devel/py-hypothesis
DEPENDS+=	${PYPKGPREFIX}-idna>=0:../../www/py-idna
DEPENDS+=	${PYPKGPREFIX}-importlib-metadata>=0:../../devel/py-importlib-metadata
DEPENDS+=	${PYPKGPREFIX}-iniconfig>=0:../../devel/py-iniconfig
DEPENDS+=	${PYPKGPREFIX}-packaging>=0:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-pluggy>=0:../../devel/py-pluggy
DEPENDS+=	${PYPKGPREFIX}-py>=0:../../devel/py-py
DEPENDS+=	${PYPKGPREFIX}-docstyle>=0:../../devel/py-docstyle
DEPENDS+=	${PYPKGPREFIX}-pyparsing>=0:../../devel/py-pyparsing
DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test
DEPENDS+=	${PYPKGPREFIX}-test-cov>=0:../../devel/py-test-cov
DEPENDS+=	${PYPKGPREFIX}-requests>=0:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-snowballstemmer>=0:../../textproc/py-snowballstemmer
DEPENDS+=	${PYPKGPREFIX}-toml>=0:../../textproc/py-toml
DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=0:../../devel/py-typing-extensions
DEPENDS+=	${PYPKGPREFIX}-urllib3>=0:../../www/py-urllib3
DEPENDS+=	${PYPKGPREFIX}-zipp>=0:../../archivers/py-zipp

USE_LANGUAGES=	# none

post-install:
	cd ${DESTDIR}${PREFIX}/bin && \
	${MV} mercantile mercantile-${PYVERSSUFFIX} || ${TRUE}

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
